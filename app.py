import streamlit as st

from resume_parser import extract_text_from_pdf
from matcher import calculate_match_score
from skills import find_missing_skills
if "history" not in st.session_state:
    st.session_state.history = []

# Page Configuration
st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
.main {
    padding-top: 1rem;
}
.big-font {
    font-size:40px !important;
    font-weight:bold;
    text-align:center;
}
.subtitle {
    text-align:center;
    color:gray;
    font-size:18px;
}
</style>
""", unsafe_allow_html=True)

# Header
st.markdown(
    '<p class="big-font">📄 AI Resume Analyzer</p>',
    unsafe_allow_html=True
)

st.markdown(
    '<p class="subtitle">Analyze your resume against job descriptions using Machine Learning</p>',
    unsafe_allow_html=True
)

st.divider()

# Layout
col1, col2 = st.columns(2)

with col1:
    uploaded_file = st.file_uploader(
        "📤 Upload Resume (PDF)",
        type=["pdf"]
    )

with col2:
    job_description = st.text_area(
        "💼 Paste Job Description",
        height=250
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
    

    st.divider()
    with st.sidebar:
        st.header("📜 Analysis History")

        if st.session_state.history:
            history_df = pd.DataFrame(st.session_state.history)
            st.dataframe(history_df)
        else:
            st.write("No history yet")

    st.subheader("📊 Resume Analysis")

    col3, col4 = st.columns(2)

    with col3:
        st.metric(
            label="Match Score",
            value=f"{score}%"
        )

    with col4:
        if score >= 80:
            st.success("Excellent Match ✅")
        elif score >= 60:
            st.warning("Good Match ⚠️")
        else:
            st.error("Needs Improvement ❌")

    st.progress(int(score))

    st.subheader("🛠 Missing Skills")

    if missing_skills:
        for skill in missing_skills:
            st.warning(skill.upper())
    else:
        st.success("No major missing skills found 🎉")

    st.subheader("💡 Recommendations")

    if score < 60:
        st.info(
            "Add more relevant keywords and technical skills from the job description."
        )
    elif score < 80:
        st.info(
            "Good resume. Consider adding more project experience and matching keywords."
        )
    else:
        st.success(
            "Your resume is highly aligned with this job role."
        )