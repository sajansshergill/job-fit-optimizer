import os
from io import BytesIO
from pdfminer.high_level import extract_text as extract_pdf
from docx import Document
import spacy

nlp = spacy.load("en_core_web_sm")

def extract_text(uploaded_file):
    ext = os.path.splitext(uploaded_file.name)[1].lower()

    if ext == ".pdf":
        uploaded_file.seek(0)  # Reset pointer
        return extract_pdf(BytesIO(uploaded_file.read()))

    elif ext == ".docx":
        uploaded_file.seek(0)
        doc = Document(uploaded_file)
        return "\n".join([para.text for para in doc.paragraphs])

    else:
        return ""

def parse_resume(uploaded_file):
    raw_text = extract_text(uploaded_file)
    doc = nlp(raw_text)

    skills = []
    tools = []
    experience = []

    for ent in doc.ents:
        if ent.label_ in ["ORG", "PRODUCT", "SKILL"]:
            skills.append(ent.text)

    for sent in doc.sents:
        if "experience" in sent.text.lower():
            experience.append(sent.text.strip())

    return {
        "name": "Candidate",
        "skills": list(set(skills)),
        "tools": list(set(tools)),
        "experience": list(set(experience)),
    }
