import re

def detect_usage_help(prompt: str) -> bool:
    keywords = ["kaise", "kahan", "use", "signup", "interview", "shortlist", "start", "register", "filter dikh", "candidate"]
    return any(word in prompt.lower() for word in keywords)

def parse_prompt(prompt: str) -> dict:
    if detect_usage_help(prompt):
        return {"intent": "usage_help", "query": prompt}

    # Default intent: CV filtering
    intent = "filter_cv"

    # Extract skills
    skills_found = re.findall(r"\b(Python|React|Node|AWS|Java|Django|SQL|Angular|ML|AI)\b", prompt, re.IGNORECASE)
    skills = list(set([s.lower() for s in skills_found]))

    # Extract experience
    experience_match = re.search(r"(\d+)\+?\s*(?:years|yrs)?", prompt)
    experience = experience_match.group(1) if experience_match else None

    return {
        "intent": intent,
        "skills": skills,
        "experience": experience
    }
