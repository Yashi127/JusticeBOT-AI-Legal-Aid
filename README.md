---
title: JusticeBot-AI Legal Aid
emoji: 🏢
colorFrom: gray
colorTo: red
sdk: gradio
sdk_version: 5.35.0
app_file: app.py
pinned: false
short_description: 'Chief Justice BOT: Legal Rights Assistant Powered by Gemini '
---

Check out the configuration reference at [https://huggingface.co/docs/hub/spaces-config-reference](https://huggingface.co/spaces/yashi127/JusticeBot-AI_Legal_Aid)

⚖️ Chief Justice BOT: Your Legal Rights Assistant

Chief Justice BOT is an AI-powered Streamlit web application designed to assist users with understanding legal content in a simplified and accessible manner. Powered by Google's Gemini model, this app provides three powerful functionalities to help users interact with legal documents and queries more effectively.

🔧 Features
1. 📜 Legal Chatbot

Ask legal questions in simple terms!

Choose a legal domain: General, Labor Law, Tenant Rights, Consumer Law, Contract Law.

Ask your legal question in natural language.

Receive an easy-to-understand answer powered by Gemini 1.5 Flash.

Maintain a history of previous Q&A for future reference.

2. 📄 Clause Analyzer
   
Upload and simplify legal documents (PDF).

Upload a PDF file containing legal clauses or content.

Automatically extract the text using PyPDF2.

Use Gemini to summarize or simplify the legal jargon for laypeople.

3. 🖼️ Document Scanner
   
Analyze legal text from scanned images.

Upload images of legal documents (.jpg, .png).

Extract text using OCR via pytesseract.

Use Gemini to provide an explanation of the extracted content in simple terms.

🧠 Tech Stack

Streamlit – Web app interface

Google Gemini (Generative AI) – Legal content simplification and explanation

PyPDF2 – PDF text extraction

pytesseract – OCR for image-to-text conversion

Pillow (PIL) – Image processing

