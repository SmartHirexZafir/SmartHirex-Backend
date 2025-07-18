from app.logic.ml_interface import get_ranked_resumes
from app.utils.redirect_helper import build_redirect_url

def build_response(parsed_data: dict) -> dict:
    intent = parsed_data.get("intent")

    if intent == "filter_cv":
        # Get mock ranked CVs (for now)
        resumes = get_ranked_resumes(parsed_data)
        redirect_url = build_redirect_url(parsed_data)

        return {
            "message": "Redirecting to filtered CV results page.",
            "redirect": redirect_url,
            "resumes_preview": resumes[:3]  # Optional preview
        }

    return {
        "message": "Sorry, I couldn't understand your query.",
        "redirect": None
    }
