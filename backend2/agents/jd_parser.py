import json
import re
from backend2.config import client, MODEL_NAME

def jd_parser(state):
    jd_text = state["jd_text"]

    prompt = f"""
Extract structured JSON from this job description:

{jd_text}

Return ONLY valid JSON:
{{
 "skills": [],
 "experience": number,
 "role": "",
 "seniority": ""
}}
"""

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[{"role": "user", "content": prompt}]
    )

    text = response.choices[0].message.content.strip()

    try:
        json_text = re.search(r"\{.*\}", text, re.DOTALL).group()
        parsed = json.loads(json_text)
    except:
        parsed = {"skills": [], "experience": 0, "role": "", "seniority": ""}

    return {"parsed_jd": parsed}