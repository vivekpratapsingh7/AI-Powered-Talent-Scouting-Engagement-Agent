def ranker(state):
    results = state["results"]

    for r in results:
        r["final_score"] = round(
            0.7 * r["match_score"] + 0.3 * r["interest_score"], 2
        )

    results.sort(key=lambda x: x["final_score"], reverse=True)

    print("RANKING DONE")

    return {"results": results}