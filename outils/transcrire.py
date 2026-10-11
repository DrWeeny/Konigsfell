"""Transcription des sessions enregistrées (WhisperX).

Deux modes :
  pistes  — un dossier d'enregistrement Craig (une piste par joueur) :
            chaque piste est transcrite, le locuteur est le pseudo du fichier.
  mix     — un fichier où toutes les voix sont mélangées : transcription
            puis séparation des voix (pyannote, demande HF_TOKEN).

Exemples :
  python transcrire.py pistes "_audio/lesucre_episode10" -o _transcripts
  python transcrire.py mix "_audio/cgi_episode1.flac" -o _transcripts --arc purge --arc cgi

Les transcripts contiennent la voix des joueurs : ils restent hors du dépôt.
"""

import argparse
import gc
import json
import os
import re
import sys
import warnings
from pathlib import Path

warnings.filterwarnings("ignore")

# Windows sans mode développeur : pas de liens symboliques dans le cache
# Hugging Face, on force la copie des fichiers.
import huggingface_hub.file_download as _hf_dl  # noqa: E402

_hf_dl.are_symlinks_supported = lambda *a, **k: False

import torch  # noqa: E402
import whisperx  # noqa: E402

# Noms propres soufflés à Whisper pour qu'il les orthographie correctement
# (orthographe de référence : dev/sessions/noms.md).
# Whisper ne garde que les ~224 derniers jetons de l'invite : on envoie le
# tronc commun, plus les arcs de la séance (--arc), pas tout d'un coup.
COMMUN = [
    "Königsfell", "les Comtes", "la Comtesse Göre", "le Comte Kette", "Überlieben", "Hahn", "Auge",
    "Gelieber", "Morgenwell", "Zeichen", "Jagenwilde", "Wildepfeife", "NassernHund", "Zotten Unterwegs",
    "Alammania", "Akkadie", "Akkadiens", "le Silence", "l'Eau Calme", "Erlöser", "Iggigi", "Ewald",
    "Abadar", "Jacques la Savate", "Gouffre", "Dédale", "Léviathan", "Kristalblum", "Trente-et-un",
    "Althaïr", "Ketnis", "Docteur Schön", "Schnee", "Johan Primo", "Lucie", "Léonilda",
]

ARCS = {
    "purge": [
        "Ussuru", "Von Murgen", "Proteo Rossano", "Nivert Iacono", "Hubert Eichel", "Ernst Stäbler",
        "Jonas Härig", "Giorgio della Gondola", "la Dévoterie", "Antonio il Pazzo", "le Roi des Damnés",
        "Oyuun la Chevelue", "Korfan Forgebrew", "horloge des Promeneurs", "la Belle Guenaude",
        "Codex Inspirationem", "Mortivières",
    ],
    "vampires": [
        "Hans d'Aragon", "Jeanne la Folle", "Arhedell Sixte", "Willensein Sieben", "Karl Fünf",
        "Enfants de la Lune", "Terre-Tapinois", "Fortecombles", "Stefano", "Agathe", "Katarina von Hahn",
        "Pilliers", "Sanglier d'Argent",
    ],
    "bal": [
        "Girolami Imondi", "Monzonite", "Serpentino", "Quartzita", "Lapis", "Sœur Svea Kalkbrenner",
        "Siriano Maschi", "Kay Kleinfeld", "le Douceâtre", "Tumo Schlafkrankheit", "Patrick Kobber",
        "Vivo l'Imbécile", "Eustosio Mormino", "Verita di Tyr", "Eleonora Abanale", "Rodolphe Vauburg",
        "Elias Havek", "Salvo Tenore", "l'ordre de l'Aube", "Transfumance", "naga",
    ],
    "orques": [
        "Sandorgul", "le Splendide", "Fremde Schäfer", "Savino", "Bartolo Melilo", "Zamana Miccuci",
        "les Inondés", "lanterne d'habitation", "l'Apôtre", "les Sirènes", "colonel Perseo", "Paolo",
        "End Station", "Gemmes de dragon",
    ],
    "reve": [
        "le Rêve", "Kitsunebi", "Sith", "le Maître des rêves", "le Maître des Voleurs", "Siffleur",
        "Zéphyr", "frère Wanderer", "Offlichtenburg", "Citadelle de l'Aube", "Procyon", "palladium",
        "Basilics", "Primordie", "Primordiaux",
    ],
    "cgi": [
        "Terry", "Cialithor", "Azula", "Zaya", "Djibril", "Suel de la Pissarrière", "Gontrad",
        "Judith", "Jardin Flamboyant", "naînerie Jaune",
    ],
}

LIMITE_INVITE = 900  # caractères, au-delà Whisper tronque le début


def glossaire(arcs=()):
    termes = list(COMMUN)
    for arc in arcs:
        termes += [t for t in ARCS[arc] if t not in termes]
    texte = ", ".join(termes) + "."
    if len(texte) > LIMITE_INVITE:
        print(f"Attention : glossaire de {len(texte)} caractères, Whisper n'en gardera que la fin.")
    return texte

# Phrases que Whisper invente sur les silences (génériques de vidéos).
HALLUCINATIONS = re.compile(
    r"sous-titr|amara\.org|merci d'avoir regardé|abonnez-vous|n'oubliez pas de vous abonner",
    re.IGNORECASE,
)

CRAIG = re.compile(r"^\d+-\d+_(.+)_\d+$")
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"


def charger_modele(nom, arcs=()):
    return whisperx.load_model(
        nom,
        DEVICE,
        compute_type="float16" if DEVICE == "cuda" else "int8",
        language="fr",
        vad_method="silero",
        asr_options={"initial_prompt": glossaire(arcs)},
    )


def transcrire(modele, aligneur, audio, batch):
    resultat = modele.transcribe(audio, batch_size=batch, language="fr")
    modele_al, meta = aligneur
    return whisperx.align(resultat["segments"], modele_al, meta, audio, DEVICE)


def hms(t):
    t = int(t)
    return f"{t // 3600:02d}:{t % 3600 // 60:02d}:{t % 60:02d}"


def fusionner(segments, ecart=2.0):
    """Regroupe les segments consécutifs d'un même locuteur."""
    blocs = []
    for s in segments:
        texte = s.get("text", "").strip()
        if not texte or HALLUCINATIONS.search(texte):
            continue
        loc = s.get("speaker", "?")
        if blocs and blocs[-1]["speaker"] == loc and s["start"] - blocs[-1]["end"] <= ecart:
            blocs[-1]["text"] += " " + texte
            blocs[-1]["end"] = s["end"]
        else:
            blocs.append({"speaker": loc, "start": s["start"], "end": s["end"], "text": texte})
    return blocs


def ecrire(blocs, sortie):
    sortie.parent.mkdir(parents=True, exist_ok=True)
    with open(sortie.with_suffix(".txt"), "w", encoding="utf-8") as f:
        for b in blocs:
            f.write(f"[{hms(b['start'])}] {b['speaker']} : {b['text']}\n")
    with open(sortie.with_suffix(".json"), "w", encoding="utf-8") as f:
        json.dump(blocs, f, ensure_ascii=False, indent=1)
    print(f"-> {sortie.with_suffix('.txt')} ({len(blocs)} répliques)")


def mode_pistes(dossier, sortie, args):
    pistes = []
    for p in sorted(Path(dossier).iterdir()):
        m = CRAIG.match(p.stem)
        if m and p.suffix.lower() in {".flac", ".wav", ".ogg", ".mp3"}:
            pistes.append((m.group(1), p))
    if not pistes:
        sys.exit(f"Aucune piste Craig dans {dossier}")
    modele = charger_modele(args.modele, args.arc)
    aligneur = whisperx.load_align_model(language_code="fr", device=DEVICE)
    segments = []
    for joueur, p in pistes:
        print(f"Transcription de {joueur}…")
        res = transcrire(modele, aligneur, whisperx.load_audio(str(p)), args.batch)
        for s in res["segments"]:
            s["speaker"] = joueur
            segments.append(s)
    segments.sort(key=lambda s: s["start"])
    ecrire(fusionner(segments), Path(sortie) / Path(dossier).name)


def mode_mix(fichiers, sortie, args):
    from huggingface_hub import get_token

    # HF_TOKEN, ou le fichier standard ~/.cache/huggingface/token
    jeton = os.environ.get("HF_TOKEN") or get_token()
    if not jeton:
        sys.exit("Jeton Hugging Face manquant : nécessaire pour séparer les voix (pyannote).")
    modele = charger_modele(args.modele, args.arc)
    aligneur = whisperx.load_align_model(language_code="fr", device=DEVICE)
    from whisperx.diarize import DiarizationPipeline, assign_word_speakers

    separateur = DiarizationPipeline(model_name=args.voix, token=jeton, device=DEVICE)
    for f in fichiers:
        cible = Path(sortie) / Path(f).stem
        if cible.with_suffix(".txt").exists() and not args.forcer:
            print(f"Déjà fait : {cible.with_suffix('.txt')}")
            continue
        print(f"Transcription de {f}…")
        audio = whisperx.load_audio(str(f))
        res = transcrire(modele, aligneur, audio, args.batch)
        voix = separateur(audio, min_speakers=args.min, max_speakers=args.max)
        res = assign_word_speakers(voix, res)
        ecrire(fusionner(res["segments"]), cible)
        del audio, res, voix
        gc.collect()
        torch.cuda.empty_cache()


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("mode", choices=["pistes", "mix"])
    ap.add_argument("entrees", nargs="+", help="dossier Craig (pistes) ou fichiers audio (mix)")
    ap.add_argument("-o", "--sortie", default="_transcripts")
    ap.add_argument("--modele", default="large-v3")
    ap.add_argument("--batch", type=int, default=16)
    ap.add_argument("--min", type=int, default=None, help="nombre minimum de voix (mix)")
    ap.add_argument("--max", type=int, default=None, help="nombre maximum de voix (mix)")
    ap.add_argument("--voix", default="pyannote/speaker-diarization-community-1",
                    help="modèle de séparation des voix (ou pyannote/speaker-diarization-3.1)")
    ap.add_argument("--forcer", action="store_true", help="refaire les transcripts existants")
    ap.add_argument("--arc", action="append", default=[], choices=sorted(ARCS),
                    help="ajoute au glossaire les noms d'un arc (répétable)")
    args = ap.parse_args()

    if args.mode == "pistes":
        for d in args.entrees:
            mode_pistes(d, args.sortie, args)
    else:
        mode_mix(args.entrees, args.sortie, args)


if __name__ == "__main__":
    main()
