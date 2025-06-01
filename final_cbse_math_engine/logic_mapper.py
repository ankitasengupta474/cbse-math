
import re

def detect(query: str) -> dict:
    q = query.lower()
    if "irrational" in q or ("prove" in q and "root" in q):
        return {"chapter": "Real Numbers", "logic": "irrationality"}
    if "hcf" in q or "lcm" in q:
        return {"chapter": "Real Numbers", "logic": "hcf_lcm"}
    return {"chapter": "Unknown", "logic": "unknown"}
