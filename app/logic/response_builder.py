import json
import os
from app.logic.ml_interface import get_ranked_resumes
from app.utils.redirect_helper import build_redirect_url

def load_usage_guide():
    path = os.path.join("app", "static", "usage_guide.json")
    with open(path, "r") as f:
        return json.load(f)

def fuzzy_match(prompt, guide):
    for q in guide:
        if any(word in prompt.lower() for word in q.lower().split()):
            return guide[q]
    return None

def build_response(parsed_data: dict) -> dict:
    intent = parsed_data.get("intent")

    if intent == "filter_cv":
        resumes = get_ranked_resumes(parsed_data)
        redirect_url = build_redirect_url(parsed_data)
        return {
            "message": "Redirecting to filtered CV results page.",
            "redirect": redirect_url,
            "resumes_preview": resumes[:3]
        }

    if intent == "usage_help":
        guide = load_usage_guide()
        reply = fuzzy_match(parsed_data.get("query", ""), guide)
        return {
            "message": reply if reply else "Sorry, is feature ke bare me mujhe info nahi mili.",
            "redirect": None
        }

    return {"message": "Sorry, I couldn't understand your query.", "redirect": None}
