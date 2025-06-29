import streamlit as st
import os
import pandas as pd
import spacy
import PyPDF2
from docx import Document
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Text cleaning with spaCy
def preprocess_text(text):
    doc = nlp(text)
    return " ".join([token.lemma_.lower() for token in doc if not token.is_stop and token.is_alpha])

# Read job description (.txt or .docx)
def read_jd(file):
    if file.type == "text/plain":
        return str(file.read(), "utf-8")
    elif file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        doc = Document(file)
        return "\n".join([para.text for para in doc.paragraphs])
    else:
        return ""

# Read resume (.txt or .pdf)
def read_resume(file):
    if file.type == "text/plain":
        return str(file.read(), "utf-8")
    elif file.type == "application/pdf":
        reader = PyPDF2.PdfReader(file)
        return " ".join(page.extract_text() for page in reader.pages if page.extract_text())
    else:
        return ""

# Streamlit UI
st.title("📄 AI-Powered Resume Screening Tool")
st.markdown("Upload a **Job Description** (`.txt` or `.docx`) and multiple **Resumes** (`.txt` or `.pdf`).")

jd_file = st.file_uploader("Upload Job Description", type=["txt", "docx"])
resume_files = st.file_uploader("Upload Resumes", type=["txt", "pdf"], accept_multiple_files=True)

if jd_file and resume_files:
    # Read and preprocess JD
    jd_text = read_jd(jd_file)
    jd_clean = preprocess_text(jd_text)

    resume_texts = []
    resume_names = []

    for file in resume_files:
        content = read_resume(file)
        if content.strip():
            cleaned = preprocess_text(content)
            resume_texts.append(cleaned)
            resume_names.append(file.name)
        else:
            st.warning(f"{file.name} appears to be empty or unreadable.")

    if resume_texts:
        # TF-IDF Vectorization and Ranking
        documents = [jd_clean] + resume_texts
        tfidf = TfidfVectorizer()
        matrix = tfidf.fit_transform(documents)
        scores = cosine_similarity(matrix[0:1], matrix[1:])[0]

        # Create DataFrame with results
        results = pd.DataFrame({
            "Resume": resume_names,
            "Similarity Score": scores
        }).sort_values(by="Similarity Score", ascending=False)

        st.success("✅ Ranking complete!")
        st.dataframe(results)

        # CSV download
        st.download_button(
            label="📥 Download Results as CSV",
            data=results.to_csv(index=False),
            file_name="resume_ranking_results.csv",
            mime="text/csv"
        )
    else:
        st.warning("No valid resume content found.")
