from fastapi import FastAPI
from backend2.graph import build_graph

app = FastAPI()
graph = build_graph()

@app.get("/")
def home():
    return {"message": "Talent Scout AI (Gemini + LangChain + LangGraph) 🚀"}

@app.post("/process")
def process(data: dict):
    result = graph.invoke({
        "jd_text": data["jd_text"],
        "parsed_jd": {},
        "results": []
    })

    return {
        "top_candidates": result["results"][:5]
    }