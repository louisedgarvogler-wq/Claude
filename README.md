# YouTube-Transkription über die Gemini-API

Das Skript `transcribe.py` transkribiert YouTube-Videos direkt über die Gemini-API. Die API akzeptiert YouTube-URLs als Videoeingabe, daher ist kein Download des Videos erforderlich. Es werden keine externen Python-Pakete benötigt (nur Standardbibliothek, Python 3.8+).

## Voraussetzung

Ein Gemini-API-Key aus Google AI Studio: https://aistudio.google.com/apikey

Hinweis: Das Gemini-Pro-Abo (Gemini-App / Google One) enthält keinen API-Zugang. Der API-Key ist davon unabhängig und im kostenlosen Kontingent nutzbar.

```bash
export GEMINI_API_KEY="dein-api-key"
```

## Verwendung

```bash
# Transkript auf stdout
python3 transcribe.py "https://www.youtube.com/watch?v=VIDEO_ID"

# In Datei speichern
python3 transcribe.py "https://www.youtube.com/watch?v=VIDEO_ID" -o transkript.md

# Mit Zeitstempeln pro Absatz
python3 transcribe.py "https://www.youtube.com/watch?v=VIDEO_ID" --timestamps

# Mehrere Videos in einem Durchlauf
python3 transcribe.py "https://youtu.be/ID1" "https://youtu.be/ID2" -o transkripte.md

# Anderes Modell (Standard: gemini-2.5-flash)
python3 transcribe.py "https://www.youtube.com/watch?v=VIDEO_ID" --model gemini-2.5-pro
```

## Grenzen

- Nur öffentliche YouTube-Videos (keine privaten oder nicht gelisteten mit Anmeldepflicht).
- Im kostenlosen API-Kontingent können pro Tag nur begrenzt Videominuten verarbeitet werden; bei langen Videos ggf. `gemini-2.5-flash` verwenden oder das Video in Abschnitten anfragen.
- Die Transkriptqualität hängt von der Audioqualität des Videos ab.
