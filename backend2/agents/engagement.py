from backend2.config import client, MODEL_NAME

def engagement(state):
    results = state["results"]

    for r in results:
        cand = r["candidate"]

        prompt = f"""
You are a job candidate.

Profile:
{cand['summary']}

Reply in 2-3 lines:
- Are you open to opportunities?
- Interest level (1-10)
- Notice period
"""

        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[{"role": "user", "content": prompt}]
        )

        r["conversation"] = response.choices[0].message.content.strip()

    return {"results": results}