from skills import SKILLS_DB

def extract_jd_skills(jd_text):

    jd_text = jd_text.lower()

    found_skills = []

    for skill in SKILLS_DB:
        if skill in jd_text:
            found_skills.append(skill)

    return found_skills