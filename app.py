import streamlit as st
from resume_parser import parse_resume
from jd_parser import parse_jd
from matcher import match_resume_to_jd
from suggestions import suggest_projects

st.set_page_config(page_title="AI-Powered Job Fit & Resume Optimizer", layout="wide")

st.title("🤖 AI-Powered Job Fit & Resume Optimizer")
st.markdown("Upload your resume (PDF or DOCX) and paste the job description to get matched skill insights, resume improvements, and project ideas!")

# Upload resume
resume_file = st.file_uploader("📄 Upload your resume (PDF or DOCX)", type=["pdf", "docx"])

# Paste JD
jd_text = st.text_area("📝 Paste the job description here", height=300)

# Trigger analysis
if st.button("🔍 Analyze Fit"):
    if resume_file is not None and jd_text.strip() != "":
        with st.spinner("Analyzing resume and job description..."):
            resume_file.seek(0)
            resume_data = parse_resume(resume_file)
            jd_data = parse_jd(jd_text)
            match_result = match_resume_to_jd(resume_data, jd_data)
            projects = suggest_projects(match_result["missing_skills"])

        # Display Results
        st.subheader("✅ Match Results")
        st.write(f"**Match Score:** {match_result['match_score']}%")

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("### 🎯 Matched Skills")
            st.write(match_result["matched_skills"] if match_result["matched_skills"] else "None")

        with col2:
            st.markdown("### 🚫 Missing Skills")
            st.write(match_result["missing_skills"] if match_result["missing_skills"] else "None")

        if match_result.get("resume_bullets_to_improve"):
            st.markdown("### ✍️ Resume Bullet Suggestions")
            for suggestion in match_result["resume_bullets_to_improve"]:
                st.write(f"- {suggestion}")

        if projects:
            st.markdown("### 🧪 Recommended Mini Projects to Fill Gaps")
            for project in projects:
                st.markdown(f"- {project}")

    else:
        st.error("Please upload a resume and paste the job description.")
