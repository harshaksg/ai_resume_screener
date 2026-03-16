import streamlit as st
from pdf_utils import extract_text_from_pdf

st.title("AI Resume Screener")

# Upload Resume
resume_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])

# JD Input Option
jd_input_type = st.radio(
    "Job Description Input",
    ["Paste Text", "Upload PDF"]
)

jd_text = ""

if jd_input_type == "Paste Text":
    jd_text = st.text_area("Paste Job Description")

elif jd_input_type == "Upload PDF":
    jd_pdf = st.file_uploader("Upload JD PDF", type=["pdf"])

    if jd_pdf:
        jd_text = extract_text_from_pdf(jd_pdf)

if st.button("Analyze"):
    st.write("Resume uploaded:", resume_file is not None)
    st.write("JD text length:", len(jd_text))