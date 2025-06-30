import streamlit as st
from PyPDF2 import PdfReader
import pytesseract
from PIL import Image
import google.generativeai as genai

# Configure Gemini
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
model = genai.GenerativeModel("models/gemini-1.5-flash")

st.set_page_config(page_title="Chief Justice BOT", layout="wide")
st.title("⚖️ Chief Justice BOT: Your Legal Rights Assistant")

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

tabs = st.tabs(["📜 Legal Chatbot", "📄 Clause Analyzer", "🖼️ Document Scanner"])

# Tab 1: Legal Chatbot
with tabs[0]:
    st.subheader("Ask a Legal Question")
    law_area = st.selectbox("Select Legal Domain", ["General", "Labor Law", "Tenant Rights", "Consumer Law", "Contract Law"])
    question = st.text_area("Enter your question")

    if st.button("Get Answer"):
        prompt = f"You are a legal assistant specializing in {law_area}. Explain the following query in simple terms:\n\n{question}"
        with st.spinner("Getting answer..."):
            try:
                response = model.generate_content(prompt)
                answer = response.text
                st.markdown("**Answer:**")
                st.write(answer)

                # Save Q&A to history
                st.session_state.chat_history.append({
                    "domain": law_area,
                    "question": question,
                    "answer": answer
                })

            except Exception as e:
                st.error(f"Error from Gemini: {e}")

    # Display chat history
    if st.session_state.chat_history:
        st.markdown("---")
        st.markdown("### 🧾 Previous Q&A")
        for i, entry in enumerate(reversed(st.session_state.chat_history), 1):
            with st.expander(f"Q{i}: {entry['question']} ({entry['domain']})"):
                st.markdown(f"**Answer:** {entry['answer']}")

# Tab 2: Clause Analyzer
with tabs[1]:
    st.subheader("Upload a Legal Clause or Document")
    uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])
    if uploaded_file:
        reader = PdfReader(uploaded_file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
        st.text_area("Extracted Clause Text", value=text, height=200)

        if st.button("Simplify Clause"):
            prompt = f"Simplify this legal clause for a layman:\n{text}"
            with st.spinner("Simplifying..."):
                try:
                    response = model.generate_content(prompt)
                    st.markdown("**Simplified Explanation:**")
                    st.write(response.text)
                except Exception as e:
                    st.error(f"Gemini Error: {e}")

# Tab 3: OCR Document Scanner
with tabs[2]:
    st.subheader("Scan and Analyze Legal Document (Image)")
    image = st.file_uploader("Upload Image (JPG/PNG)", type=["jpg", "png"])
    if image:
        img = Image.open(image)
        text = pytesseract.image_to_string(img)
        st.text_area("Extracted Text", value=text, height=200)

        if st.button("Explain Extracted Text"):
            prompt = f"Explain this legal content simply:\n{text}"
            with st.spinner("Explaining..."):
                try:
                    response = model.generate_content(prompt)
                    st.markdown("**Explanation:**")
                    st.write(response.text)
                except Exception as e:
                    st.error(f"Gemini Error: {e}")
