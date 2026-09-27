# Campus AI Assistant

A small Streamlit campus information assistant. It reads local college information from `college_info.txt`, answers common questions in English/simple Hinglish, and keeps the conversation in the browser session.

## Features

- Quick questions for common campus topics
- Rule-based question matching for English and common Hinglish terms
- Typo-tolerant matching for a single unclear topic and combined answers for questions naming multiple topics
- Answers grounded in the local knowledge file, with a clear fallback when information is missing
- Placeholder protection for unconfirmed contact and address fields
- Knowledge section overview, conversation counter, clear-chat control, and transcript download
- No API key, paid model, or external database required

## Run locally (Windows PowerShell)

Open PowerShell in this project folder and run:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
streamlit run App.py
```

The app opens in your browser. Stop it with `Ctrl+C` in the terminal.

If PowerShell blocks environment activation, you can invoke the virtual environment's Python directly:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m streamlit run App.py
```

## Run locally (macOS/Linux)

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
streamlit run App.py
```

## Update campus information

Edit `college_info.txt`. Use a section heading ending in a colon, then put one fact on each following line:

```text
COURSES:
Program name
Another program

LIBRARY:
Opening time: confirm with the university before publishing
```

Keep the file beside `App.py`. The app loads it when it starts. Only add information confirmed by the university; the details originally supplied with this project have not been independently verified. Replace contact/address placeholders only with official details. Avoid publishing personal student data or secrets.

## Project files

- `App.py` — Streamlit interface
- `assistant.py` — knowledge-file parser and question-matching logic
- `college_info.txt` — editable local campus information
- `requirements.txt` — Python dependency list

## Current scope

This is a keyword/rule-based information assistant, not a generative AI model and not an official university service. It does not fetch live notices, admissions, fee updates, exam schedules, or contact details. For changing or important information, check an official university channel.
