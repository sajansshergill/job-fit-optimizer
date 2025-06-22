from jd_parser import parse_job_description

jd_text = """
We are looking for a Data Scientist with experience in Python, SQL, and machine learning.
Responsibilities include building predictive models, performing A/B testing, and visualizing data in Tableau or Power BI.
Familiarity with cloud platforms like AWS is a plus.
"""

result = parse_job_description(jd_text)
print(result)
