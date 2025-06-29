# 📄 AI-Powered Resume Screening Tool

## 🔍 Objective

This project automates the process of screening resumes by ranking them based on how well they match a given job description using NLP techniques.

---

## ✅ Features

- Upload **job descriptions** in `.txt` or `.docx` format
- Upload multiple **resumes** in `.pdf` or `.txt` format
- NLP-based **text preprocessing** using `spaCy`
- Text similarity comparison using **TF-IDF + Cosine Similarity**
- Ranks resumes based on their relevance to the job description
- **Streamlit UI** for easy interaction
- Download results as **CSV file**

---

## 🛠 Tech Stack

| Tool        | Purpose                          |
|-------------|----------------------------------|
| Python      | Core programming language        |
| spaCy       | NLP preprocessing                |
| scikit-learn| TF-IDF + Cosine similarity       |
| Streamlit   | Interactive web UI               |
| PyPDF2      | PDF resume parsing               |
| python-docx | DOCX job description reading     |
| pandas      | Data handling and CSV export     |

---

## 📁 Folder Structure
AI_Powered_Resume_Screenimg_Tool/
├── resume_screening_app.py
├── requirements.txt
├── job_description.docx
├── resumes/
│ ├── resume_1.pdf
│ ├── resume_2.txt


---

## ▶️ How to Run

### 🔧 Step 1: Install requirements

->bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm

#Run the app
streamlit run resume_screening_app.py

📌 Example Use Case
HR teams or recruiters can automate resume screening by uploading job descriptions and a batch of resumes. The app ranks candidates by how closely their skills and experience align with the job requirements.

📥 Output
Ranked resume list shown in the browser

Downloadable CSV report: resume_ranking_results.csv

👨‍💻 Author
Shaik Fayaz Ahamed
B.Tech CSE (Data Science) & (Artificial Intelligence)
Internship Project – June 2025
