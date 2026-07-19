import streamlit as st
from src.database import populate_database
from src.generator import generate_quiz

# Initialize database
populate_database()

st.set_page_config(
    page_title="AI Sports Quiz Generator",
    page_icon="🏆",
    layout="centered"
)

st.title("🏆 AI-Powered Sports Quiz Generator")

sport = st.selectbox(
    "Select Sport",
    ["Cricket", "Football", "Badminton", "Basketball", "Tennis"]
)

difficulty = st.selectbox(
    "Select Difficulty",
    ["Easy", "Medium", "Hard"]
)

if "quiz" not in st.session_state:
    st.session_state.quiz = ""

col1, col2 = st.columns(2)

with col1:
    if st.button("Generate Quiz", use_container_width=True):
        with st.spinner("Generating Quiz..."):
            st.session_state.quiz = generate_quiz(sport, difficulty)

with col2:
    if st.button("Regenerate Quiz", use_container_width=True):
        with st.spinner("Generating New Quiz..."):
            st.session_state.quiz = generate_quiz(sport, difficulty)

if st.session_state.quiz:
    st.markdown("---")
    st.subheader("Generated Quiz")

    st.text_area(
        "Quiz",
        value=st.session_state.quiz,
        height=500
    )

    with st.expander("🔍 Retrieved Knowledge"):
        st.write("Historical facts were retrieved from ChromaDB.")
        st.write("Recent information was retrieved from DuckDuckGo.")