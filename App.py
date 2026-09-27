from __future__ import annotations

from pathlib import Path

import streamlit as st

from assistant import SUPPORTED_TOPICS, answer_question, load_knowledge


APP_DIR = Path(__file__).resolve().parent
KNOWLEDGE_FILE = APP_DIR / "college_info.txt"
KNOWLEDGE = load_knowledge(KNOWLEDGE_FILE)
st.set_page_config(
    page_title="Jagannath University | Campus Assistant",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');

    html, body, [class*="css"], .stApp {
        font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
    }

    .stApp {
        background: linear-gradient(180deg, #f8faff 0%, #eef3fc 100%);
    }

    [data-testid="stHeader"] {
        background: rgba(248, 250, 255, 0.85);
        backdrop-filter: blur(12px);
    }

    .hero {
        padding: 36px 38px;
        border-radius: 24px;
        color: white;
        background: linear-gradient(135deg, #0d2757 0%, #1a448d 50%, #4361ee 100%);
        box-shadow: 0 16px 40px rgba(13, 39, 87, 0.22);
        margin: 4px 0 24px;
        position: relative;
        overflow: hidden;
    }

    .hero-badge {
        display: inline-flex;
        align-items: center;
        gap: 6px;
        background: rgba(255, 255, 255, 0.16);
        backdrop-filter: blur(8px);
        padding: 6px 14px;
        border-radius: 999px;
        font-size: 13px;
        font-weight: 600;
        letter-spacing: 0.02em;
        margin-bottom: 12px;
        border: 1px solid rgba(255, 255, 255, 0.25);
    }

    .hero h1 {
        color: white !important;
        margin: 0;
        font-size: clamp(26px, 3.6vw, 38px);
        font-weight: 800;
        letter-spacing: -0.03em;
        line-height: 1.2;
    }

    .hero p {
        color: #dbe4ff !important;
        margin: 10px 0 0;
        font-size: 16px;
        font-weight: 400;
        max-width: 650px;
        line-height: 1.5;
    }

    div[data-testid="stMetric"] {
        background: rgba(255, 255, 255, 0.85);
        backdrop-filter: blur(10px);
        border: 1px solid #e1e7f5;
        padding: 18px 20px;
        border-radius: 18px;
        box-shadow: 0 4px 20px rgba(18, 38, 77, 0.05);
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }

    div[data-testid="stMetric"]:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 24px rgba(18, 38, 77, 0.09);
    }

    [data-testid="stSidebar"] {
        background: #ffffff;
        border-right: 1px solid #e8eef8;
    }

    .stButton > button {
        border-radius: 12px;
        font-weight: 600;
        transition: all 0.2s ease;
        border: 1px solid #dce4f2;
    }

    .stButton > button:hover {
        border-color: #4361ee;
        color: #4361ee;
        box-shadow: 0 4px 12px rgba(67, 97, 238, 0.15);
    }

    [data-testid="stChatMessage"] {
        background: rgba(255, 255, 255, 0.9);
        border-radius: 18px;
        border: 1px solid #e8edf5;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.03);
        margin-bottom: 12px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

if "messages" not in st.session_state:
    st.session_state.messages = []
if "pending_question" not in st.session_state:
    st.session_state.pending_question = None


with st.sidebar:
    st.title("🎓 Campus Assistant")
    st.caption("Jagannath University information guide")
    st.divider()
    st.subheader("Quick questions")
    for topic, question in SUPPORTED_TOPICS.items():
        if st.button(topic, key=f"quick_{topic}", use_container_width=True):
            st.session_state.pending_question = question

    st.divider()
    st.markdown("**Knowledge file**")
    if KNOWLEDGE:
        st.success(f"{len(KNOWLEDGE)} sections loaded")
        if any("REPLACE_WITH_" in item.upper() for values in KNOWLEDGE.values() for item in values):
            st.warning("Contact/address placeholders need official details before public sharing.")
    else:
        st.warning("college_info.txt missing or empty")

    if st.button("🗑️ Clear conversation", use_container_width=True):
        st.session_state.messages = []
        st.session_state.pending_question = None
        st.rerun()


st.markdown(
    """
    <section class="hero">
      <div class="hero-badge">🎓 Official Campus Knowledge Guide</div>
      <h1>Jagannath University Campus Assistant</h1>
      <p>Instant answers on courses, timings, admissions, exams, contacts & facilities. Ask in English or simple Hinglish!</p>
    </section>
    """,
    unsafe_allow_html=True,
)

total_questions = sum(message["role"] == "user" for message in st.session_state.messages)
metric1, metric2, metric3 = st.columns(3)
with metric1:
    st.metric("Information sections", len(KNOWLEDGE))
with metric2:
    st.metric("Questions this chat", total_questions)
with metric3:
    st.metric("Assistant mode", "Knowledge-based")

with st.expander("Browse available information"):
    if KNOWLEDGE:
        selected_section = st.selectbox(
            "Choose a category",
            list(KNOWLEDGE),
            format_func=lambda key: key.title(),
        )
        details = [
            item for item in KNOWLEDGE[selected_section]
            if "REPLACE_WITH_" not in item.upper()
        ]
        if details:
            for detail in details:
                st.markdown(f"- {detail}")
        else:
            st.info("Verified details have not been added for this category yet.")

st.subheader("💬 Ask a question")
st.caption("Answers come only from the local college_info.txt file. Verify important details with the university.")

if not st.session_state.messages:
    st.info("Welcome! Try a quick question from the sidebar or type a question below.")

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        if message.get("topic"):
            st.caption(f"Knowledge section: {message['topic']}")

typed_question = st.chat_input("Example: library timing kya hai?")
question = typed_question or st.session_state.pending_question
if question:
    st.session_state.pending_question = None
    answer, matched_topic = answer_question(question, KNOWLEDGE)
    st.session_state.messages.extend(
        [
            {"role": "user", "content": question},
            {"role": "assistant", "content": answer, "topic": matched_topic},
        ]
    )
    st.rerun()

if st.session_state.messages:
    transcript = "\n\n".join(
        f"{'You' if item['role'] == 'user' else 'Campus Assistant'}: {item['content']}"
        for item in st.session_state.messages
    )
    st.download_button(
        "⬇️ Download conversation",
        data=transcript,
        file_name="campus_assistant_conversation.txt",
        mime="text/plain",
    )

st.divider()
st.caption(
    "This is a knowledge-based student project, not an official university service. "
    "Admission, examination, fees, timings and contact details can change; confirm them through official channels."
)
