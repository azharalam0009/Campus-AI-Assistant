# 🎓 AI Campus Assistant

A beginner-friendly college information assistant built with **Python + Streamlit**.

## Features

- 🎓 College / university information
- 📚 Courses and branches
- 📖 Library information
- 🍽️ Canteen information
- 📝 Admission information
- 📅 Examination information
- 🏢 Office information
- 📞 Contact information
- 📍 Location information
- 🏫 Campus facilities
- 🎓 Student services
- 💬 Chat history
- ⚡ Quick-question sidebar
- 🗑️ Clear chat
- 📄 College knowledge stored separately in `college_info.txt`

## Project Structure

```text
AI-Campus-Assistant/
├── app.py
├── college_info.txt
├── requirements.txt
├── README.md
└── .gitignore
```

## Run Locally

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Start the app

```bash
streamlit run app.py
```

### 3. Open

Streamlit will show a local URL such as:

```text
http://localhost:8501
```

## Important

Replace the placeholder contact and location information in `college_info.txt` with verified official information before publishing the project.

## Current Version

This version uses a lightweight rule/keyword-based response engine and a local text knowledge file. It is a working foundation for a future RAG/LLM version.

## Future Upgrades

- PDF upload and text extraction
- RAG-based document search
- LLM integration
- Source citations
- Authentication
- Admin dashboard
- Deployment
