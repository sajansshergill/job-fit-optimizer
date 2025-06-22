import os
import spacy
from pdfminer.high_level import extract_text as extract_pdf
from docx import Document

nlp = spacy.load("en_core_web_sm")

def extract_text_from_docx(docx_path):
    doc = Document(docx_path)
    return "\n".join([para.text for para in doc.paragraphs])

def extract_text(file_path):
    ext = os.path.splitext(file_path)[1].lower()
    if ext == '.pdf':
        return extract_pdf(file_path)
    elif ext == '.docx':
        return extract_text_from_docx(file_path)
    else:
        raise ValueError("Unsupported file format")

def extract_resume_info(text):
    doc = nlp(text)
    skills = []
    tools = []
    experience = []

    for ent in doc.ents:
        if ent.label_ in ['ORG', 'PRODUCT', 'SKILL']:
            tools.append(ent.text)
        elif ent.label_ == 'PERSON':
            continue
        elif ent.label_ == 'WORK_OF_ART':
            skills.append(ent.text)

    # Dummy parsing logic for now — update with real patterns later
    for sent in doc.sents:
        if '-' in sent.text or '•' in sent.text:
            experience.append(sent.text.strip())

    return {
        'skills': list(set(skills)),
        'tools': list(set(tools)),
        'experience': experience
    }

def parse_resume(file_path):
    raw_text = extract_text(file_path)
    return extract_resume_info(raw_text)
