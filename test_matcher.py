from resume_parser import parse_resume
from jd_parser import parse_job_description
from matcher import match_resume_to_jd

# 👇 Replace with your real file path
resume_data = parse_resume("/Users/sajanshergill/Desktop/job-fit-optimizer/data/sample_resumes/SajanSinghShergill-RESUME(On-Campus).pdf")

jd_text = """
We are looking for a data analyst skilled in SQL, Python, Tableau, and A/B testing.
You should be able to analyze customer behavior, run statistical experiments, and visualize data.
Knowledge of Power BI and Excel is a plus.
"""

jd_data = parse_job_description(jd_text)

match_result = match_resume_to_jd(resume_data, jd_data)

print("\nMatch Result Summary:")
print(match_result)
