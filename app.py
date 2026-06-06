import streamlit as st

from resume_parser import extract_text_from_pdf
from matcher import calculate_match_score
from skills import find_missing_skills

st.title("AI Resume Analyzer")

uploaded_file = st.file_uploader(
    "Upload Resume (PDF)",
    type=["pdf"]
)

job_description = st.text_area(
    "Paste Job Description"
)

if uploaded_file and job_description:

    resume_text = extract_text_from_pdf(uploaded_file)

    score = calculate_match_score(
        resume_text,
        job_description
    )

    missing_skills = find_missing_skills(
        resume_text,
        job_description
    )

    st.subheader("Match Score")
    st.success(f"{score}%")

    st.subheader("Missing Skills")

    if missing_skills:
        for skill in missing_skills:
            st.write(f"❌ {skill}")
    else:
        st.write("✅ No major missing skills")