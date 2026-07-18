import os
from openai import OpenAI


def build_prompt(resume: dict, job: dict) -> str:
    return f"""You are an expert career coach. Write a professional, personalized cover letter
for the following candidate applying to the specified role.

CANDIDATE RESUME:
- Name: {resume.get("name", "N/A")}
- Experience: {resume.get("experience", "N/A")}
- Skills: {", ".join(resume.get("skills", []))}
- Projects: {", ".join(resume.get("projects", []))}

JOB DETAILS:
- Title: {job.get("title", "N/A")}
- Requirements: {", ".join(job.get("requirements", []))}

INSTRUCTIONS:
1. Address how the candidate's experience aligns with the job requirements.
2. Highlight relevant projects that demonstrate capability.
3. Match the candidate's skills to the job's needs specifically.
4. Keep the tone professional but personable.
5. Keep it under 300 words.
"""


def generate_cover_letter(resume: dict, job: dict) -> str:
    client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
    prompt = build_prompt(resume, job)

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a professional cover letter writer."},
            {"role": "user", "content": prompt},
        ],
        temperature=0.7,
        max_tokens=500,
    )

    return response.choices[0].message.content
