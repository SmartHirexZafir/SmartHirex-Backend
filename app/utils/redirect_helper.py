from urllib.parse import urlencode

def build_redirect_url(filters: dict) -> str:
    base_url = "/filtered-results"
    params = {}

    if filters.get("skills"):
        params["skills"] = ",".join(filters["skills"])

    if filters.get("experience"):
        params["experience"] = filters["experience"]

    return f"{base_url}?{urlencode(params)}"
