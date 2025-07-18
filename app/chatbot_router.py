from fastapi import APIRouter, Request
from app.logic.intent_parser import parse_prompt
from app.logic.response_builder import build_response

router = APIRouter()

@router.post("/query")
async def handle_chatbot_query(request: Request):
    data = await request.json()
    prompt = data.get("prompt", "")

    if not prompt.strip():
        return {"message": "Prompt is empty."}

    parsed = parse_prompt(prompt)
    response = build_response(parsed)
    return response
