# This is a dummy interface simulating the ML model

def get_ranked_resumes(filters: dict):
    # This will be replaced with real ML API call later
    # For now we return mock data

    # Example logic: If React is in skills, return different result
    if "react" in filters.get("skills", []):
        return [
            {"name": "Ali Khan", "score": 0.91, "skills": ["React", "JavaScript"]},
            {"name": "Sana Riaz", "score": 0.87, "skills": ["React", "Node.js"]},
            {"name": "Bilal Ahmed", "score": 0.85, "skills": ["React", "Redux"]}
        ]
    else:
        return [
            {"name": "Usman Tariq", "score": 0.89, "skills": ["Python", "Django"]},
            {"name": "Ayesha Malik", "score": 0.88, "skills": ["Java", "Spring"]},
            {"name": "Zainab Ali", "score": 0.83, "skills": ["SQL", "BI"]}
        ]
