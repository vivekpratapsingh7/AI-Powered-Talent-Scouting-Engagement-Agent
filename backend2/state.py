from typing import TypedDict, List, Dict, Any

class TalentState(TypedDict):
    jd_text: str
    parsed_jd: Dict[str, Any]
    candidates: List[Dict]
    results: List[Dict]