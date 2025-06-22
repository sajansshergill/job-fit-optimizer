import openai
from dotenv import load_dotenv
import os
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def rewrite_bullet_point(bullet, jd_text, missing_skills=[]):
    prompt = f"""
You are a professional resume writer. Here's a job description:
\"\"\"
{jd_text}
\"\"\"

Below is a resume bullet point:
\"{bullet}\"

Rewrite the bullet to better match the job description, making it more results-oriented and incorporating these missing skills/tools if relevant: {", ".join(missing_skills)}.

Return only the rewritten bullet in one line.
"""

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # or "gpt-4"
        messages=[
            {"role": "system", "content": "You are a resume optimization assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=150
    )

    return response['choices'][0]['message']['content'].strip()
