import streamlit as st
from pdf_utils import extract_text_from_pdf
from resume_parser import extract_resume_skills
from jd_parser import extract_jd_skills
from similarity_engine import compute_similarity, match_score, find_missing_skills

st.title("AI Resume Screener")

resume_file = st.file_uploader("Upload Resume", type=["pdf"])

jd_input_type = st.radio("JD Input Type", ["Paste Text", "Upload PDF"])

jd_text = ""

if jd_input_type == "Paste Text":
    jd_text = st.text_area("Paste Job Description")

elif jd_input_type == "Upload PDF":
    jd_pdf = st.file_uploader("Upload JD PDF", type=["pdf"])

    if jd_pdf:
        jd_text = extract_text_from_pdf(jd_pdf)

if st.button("Analyze"):

    if resume_file and jd_text:

        resume_skills, resume_text = extract_resume_skills(resume_file)

        jd_skills = extract_jd_skills(jd_text)

        similarity = compute_similarity(resume_text, jd_text)

        score = match_score(similarity)

        missing_skills = find_missing_skills(resume_skills, jd_skills)

        st.subheader("Match Score")
        st.write(f"{score}%")

        st.subheader("Missing Skills")
        st.write(missing_skills)