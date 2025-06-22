import spacy

nlp = spacy.load("en_core_web_sm")

def parse_jd(jd_text):
    """
    Parses the job description and extracts skills, tools, responsibilities using NLP.
    Returns a dictionary of relevant keywords.
    """
    doc = nlp(jd_text)

    # Extract key noun chunks and named entities
    noun_phrases = [chunk.text.strip().lower() for chunk in doc.noun_chunks]
    keywords = [token.text.strip().lower() for token in doc if token.pos_ in ["NOUN", "PROPN", "ADJ"]]

    # Combine and deduplicate
    key_terms = list(set(noun_phrases + keywords))

    # Filter out common stop words and irrelevant short words
    key_terms = [kw for kw in key_terms if len(kw) > 2 and not kw in nlp.Defaults.stop_words]

    return {
        "required_skills": key_terms,
        "responsibilities": key_terms,
        "tools": key_terms
    }
