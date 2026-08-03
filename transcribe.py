#!/usr/bin/env python3
"""Transkribiert YouTube-Videos über die Gemini-API.

Die Gemini-API akzeptiert YouTube-URLs direkt als Videoeingabe,
d. h. das Video muss nicht heruntergeladen werden.

Voraussetzung: Umgebungsvariable GEMINI_API_KEY
(API-Key erstellen unter https://aistudio.google.com/apikey)

Verwendung:
    python3 transcribe.py <youtube-url> [weitere-urls ...]
    python3 transcribe.py <youtube-url> -o transkript.md
    python3 transcribe.py <youtube-url> --model gemini-2.5-pro
    python3 transcribe.py <youtube-url> --timestamps
"""

import argparse
import json
import os
import re
import sys
import urllib.error
import urllib.request

API_URL = "https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent"
DEFAULT_MODEL = "gemini-2.5-flash"

YOUTUBE_URL_RE = re.compile(
    r"^https?://(www\.)?(youtube\.com/(watch\?v=|shorts/|live/)|youtu\.be/)[\w-]{6,}"
)

PROMPT_PLAIN = (
    "Transkribiere den gesprochenen Inhalt dieses Videos vollständig und wortgetreu. "
    "Gib ausschließlich das Transkript aus, ohne Kommentare oder Zusammenfassung. "
    "Behalte die Originalsprache des Videos bei."
)

PROMPT_TIMESTAMPS = (
    "Transkribiere den gesprochenen Inhalt dieses Videos vollständig und wortgetreu. "
    "Setze vor jeden Absatz einen Zeitstempel im Format [MM:SS]. "
    "Gib ausschließlich das Transkript aus, ohne Kommentare oder Zusammenfassung. "
    "Behalte die Originalsprache des Videos bei."
)


def transcribe(url: str, api_key: str, model: str, timestamps: bool) -> str:
    prompt = PROMPT_TIMESTAMPS if timestamps else PROMPT_PLAIN
    body = {
        "contents": [
            {
                "parts": [
                    {"file_data": {"file_uri": url}},
                    {"text": prompt},
                ]
            }
        ]
    }
    request = urllib.request.Request(
        API_URL.format(model=model),
        data=json.dumps(body).encode("utf-8"),
        headers={
            "Content-Type": "application/json",
            "x-goog-api-key": api_key,
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=600) as response:
            data = json.load(response)
    except urllib.error.HTTPError as error:
        detail = error.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"API-Fehler {error.code}: {detail}") from error

    try:
        parts = data["candidates"][0]["content"]["parts"]
    except (KeyError, IndexError) as error:
        raise RuntimeError(f"Unerwartete API-Antwort: {json.dumps(data)[:500]}") from error

    return "".join(part.get("text", "") for part in parts).strip()


def main() -> int:
    parser = argparse.ArgumentParser(description="YouTube-Videos über die Gemini-API transkribieren")
    parser.add_argument("urls", nargs="+", help="Eine oder mehrere YouTube-URLs")
    parser.add_argument("-o", "--output", help="Transkript in Datei schreiben statt auf stdout")
    parser.add_argument("--model", default=DEFAULT_MODEL, help=f"Gemini-Modell (Standard: {DEFAULT_MODEL})")
    parser.add_argument("--timestamps", action="store_true", help="Zeitstempel pro Absatz einfügen")
    args = parser.parse_args()

    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("Fehler: Umgebungsvariable GEMINI_API_KEY ist nicht gesetzt.", file=sys.stderr)
        print("API-Key erstellen: https://aistudio.google.com/apikey", file=sys.stderr)
        return 1

    for url in args.urls:
        if not YOUTUBE_URL_RE.match(url):
            print(f"Fehler: Keine gültige YouTube-URL: {url}", file=sys.stderr)
            return 1

    sections = []
    for url in args.urls:
        print(f"Transkribiere: {url}", file=sys.stderr)
        try:
            transcript = transcribe(url, api_key, args.model, args.timestamps)
        except RuntimeError as error:
            print(f"Fehler bei {url}: {error}", file=sys.stderr)
            return 1
        sections.append(f"# {url}\n\n{transcript}" if len(args.urls) > 1 else transcript)

    result = "\n\n---\n\n".join(sections) + "\n"

    if args.output:
        with open(args.output, "w", encoding="utf-8") as file:
            file.write(result)
        print(f"Transkript gespeichert: {args.output}", file=sys.stderr)
    else:
        print(result)

    return 0


if __name__ == "__main__":
    sys.exit(main())
