from pyresparser import ResumeParser

def parse_resume(resume_path):
    data = ResumeParser(resume_path).get_extracted_data()

    skills = data.get("skills", [])

    return {
        "name": data.get("name"),
        "skills": skills,
        "experience": data.get("experience")
    }