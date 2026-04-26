import re
from backend2.config import client, MODEL_NAME

def interest_scorer(state):
    results = state["results"]

    for r in results:
        convo = r["conversation"]

        prompt = f"""
Rate interest from 0 to 1:

{convo}

Return ONLY a number.
"""

        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[{"role": "user", "content": prompt}]
        )

        text = response.choices[0].message.content.strip()

        try:
            score = float(re.findall(r"\d*\.?\d+", text)[0])
            score = max(0, min(score, 1))
        except:
            score = 0.5

        r["interest_score"] = round(score, 2)

    return {"results": results}