from pdf_utils import extract_text_from_pdf
import spacy

nlp = spacy.load("en_core_web_sm")

def extract_resume_skills(resume_file):

    text = extract_text_from_pdf(resume_file)

    doc = nlp(text)

    skills = []

    for token in doc:
        if token.pos_ == "NOUN" or token.pos_ == "PROPN":
            skills.append(token.text.lower())

    return list(set(skills)), text