import streamlit as st
import os
from crew.setup_crew import initialize_crew  # You define this earlier
from tools.build_rag_chatbot import build_vector_store, build_qa_chain  # Import RAG logic
from dotenv import load_dotenv
import tempfile

# Load Groq API Key
load_dotenv()

st.set_page_config(page_title="📚 Autonomous Research Assistant", layout="wide")

# App title
st.title("📖 Autonomous RAG Research Assistant")

# Sidebar upload
st.sidebar.header("Upload Research Paper")
uploaded_file = st.sidebar.file_uploader("Upload a PDF", type=["pdf"])

# Temporary file save
if uploaded_file:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(uploaded_file.read())
        tmp_path = tmp_file.name
        st.sidebar.success(f"Uploaded: {uploaded_file.name}")

# Button to run CrewAI pipeline
if uploaded_file and st.sidebar.button("🚀 Run Research Agents"):
    st.info("Running the Crew to parse, explain, cite, and visualize...")
    crew = initialize_crew()
    result = crew.kickoff(inputs={"pdf_path": tmp_path})
    st.success("✅ Booklet generated!")

    if os.path.exists("output/booklet.pdf"):
        with open("output/booklet.pdf", "rb") as f:
            st.download_button(
                label="📄 Download Research Booklet",
                data=f,
                file_name="research_booklet.pdf",
                mime="application/pdf"
            )

    # Load simplified sections for chatbot
    # (Assuming you save them during crew execution to a known file or return it)
    import json
    if os.path.exists("output/simplified_sections.json"):
        with open("output/simplified_sections.json", "r") as f:
            simplified = json.load(f)

        # Build RAG chatbot
        st.session_state.vectorstore = build_vector_store(simplified)
        st.session_state.qa_chain = build_qa_chain(st.session_state.vectorstore)

# Chatbot Section
if "qa_chain" in st.session_state:
    st.markdown("---")
    st.subheader("💬 Ask Anything About the Paper")

    user_input = st.text_input("Type your question:")
    if user_input:
        response = st.session_state.qa_chain.run(user_input)
        st.markdown(f"**🧠 Answer:** {response}")

elif uploaded_file:
    st.info("⬅️ Upload the paper and run agents to activate chatbot.")

else:
    st.info("⬅️ Start by uploading a research paper on the left.")

