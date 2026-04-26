from backend2.services.candidate_db import load_candidates

def matcher(state):
    jd = state["parsed_jd"]
    candidates = load_candidates()

    results = []

    jd_skills = set(jd.get("skills", []))
    jd_exp = jd.get("experience", 1)

    for cand in candidates:
        cand_skills = set(cand["skills"])

        skill_score = len(jd_skills & cand_skills) / max(len(jd_skills), 1)
        exp_score = min(cand["experience"] / jd_exp, 1)

        match_score = 0.6 * skill_score + 0.4 * exp_score

        results.append({
            "candidate": cand,
            "match_score": round(match_score, 2),
            "explanation": {
                "matched_skills": list(jd_skills & cand_skills),
                "missing_skills": list(jd_skills - cand_skills)
            }
        })

    print("MATCHED:", len(results))

    return {"results": results}