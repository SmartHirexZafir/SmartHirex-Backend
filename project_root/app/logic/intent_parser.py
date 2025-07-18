import re

def parse_prompt(prompt: str) -> dict:
    # Intent assumed to be "filter_cv" for now
    intent = "filter_cv"

    # Skill extraction (you can expand this list or use NLP later)
    skills_found = re.findall(r"\b(Python|React|Node|AWS|Java|Django|SQL|Angular|ML|AI)\b", prompt, re.IGNORECASE)
    skills = list(set([s.lower() for s in skills_found]))

    # Experience extraction
    experience_match = re.search(r"(\d+)\+?\s*(?:years|yrs)?", prompt)
    experience = experience_match.group(1) if experience_match else None

    return {
        "intent": intent,
        "skills": skills,
        "experience": experience
    }
