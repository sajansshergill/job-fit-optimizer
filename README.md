# 🧠 AI-Powered Job Fit & Resume Optimizer

---

## 🔍 Overview
The AI-Powered Job Fit & Resume Optimizer is a smart web app that helps job seekers:

- Analyze how well their resume matches a given job description

- Get suggestions to rewrite resume bullet points for better alignment

- Identify missing skills and recommend personalized project ideas

Built with Python, NLP, Streamlit, and powerful text matching techniques, this tool helps candidates improve their resumes and job prospects efficiently.

## 💡 Features
- 📄 Resume Parser: Extracts and cleans content from .pdf and .docx resumes using pdfminer and python-docx

- 📝 Job Description Parser: Extracts required skills from job descriptions using spaCy's NLP pipeline

- 🤖 Smart Matching: Compares resume content with job requirements using TF-IDF, fuzzy matching, and spaCy similarity

- ✨ Resume Rewriting Suggestions: Recommends improved bullet points to enhance clarity and relevance

- 🧩 Project Suggestions: Suggests data, ML, or domain-specific portfolio projects based on skill gaps

- 🎛️ Streamlit UI: Intuitive interface to upload files, view scores, and interact with recommendations

## 🗂️ Folder Structure
job-fit-optimizer/
│
├── app.py                     # Streamlit application
├── resume_parser.py           # Resume extraction logic
├── jd_parser.py               # Job description extraction logic
├── matcher.py                 # Resume vs JD matching engine
├── rewriter.py                # Resume improvement suggestions
├── suggestions.py             # Project ideas based on skill gaps
├── test.py                    # Unit test for resume parser
├── test_matcher.py            # Unit test for skill matcher
├── requirements.txt           # All required dependencies
└── README.md                  # You're here!


📦 Requirements
- Python 3.8+

- Libraries:

  - streamlit

  - spacy

  - scikit-learn

  - pdfminer.six

  - python-docx

  - fuzzywuzzy

  - nltk
 
---

## 👨‍💻 Author
Built by Sajan Shergill,
Aspiring data scientist
