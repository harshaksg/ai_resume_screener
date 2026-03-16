from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer('all-MiniLM-L6-v2')

def compute_similarity(resume_text, jd_text):

    resume_embedding = model.encode(resume_text)
    jd_embedding = model.encode(jd_text)

    score = cosine_similarity([resume_embedding], [jd_embedding])[0][0]

    return score

def match_score(similarity):
    return round(similarity * 100, 2)

def find_missing_skills(resume_skills, jd_skills):

    resume_set = set(resume_skills)
    jd_set = set(jd_skills)

    missing = jd_set - resume_set

    return list(missing)