from pdf_utils import extract_text_from_pdf
from skills import SKILLS_DB

def extract_resume_skills(resume_file):

    text = extract_text_from_pdf(resume_file).lower()

    found_skills = []

    for skill in SKILLS_DB:
        if skill in text:
            found_skills.append(skill)

    return found_skills, text