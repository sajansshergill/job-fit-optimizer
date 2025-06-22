from resume_parser import parse_resume
from jd_parser import parse_job_description
from matcher import match_resume_to_jd
from rewrite_helper import rewrite_bullet_point

resume_data = parse_resume("/Users/sajanshergill/Desktop/job-fit-optimizer/data/sample_resumes/SajanSinghShergill-RESUME(On-Campus).pdf")
jd_text = """
We are hiring a Data Analyst with experience in Python, SQL, Tableau, and A/B testing. 
Must be skilled in analyzing customer behavior, producing dashboards, and statistical testing.
"""

jd_data = parse_job_description(jd_text)
match_result = match_resume_to_jd(resume_data, jd_data)

print("Original Experience:")
sample_experience = resume_data['experience'][:1]  # pick one bullet to test

for bullet in sample_experience:
    rewritten = rewrite_bullet_point(
        bullet=bullet,
        jd_text=jd_text,
        missing_skills=match_result['missing_skills']
    )
    print(f"\n🔹 Original: {bullet}")
    print(f"✅ Rewritten: {rewritten}")
