from fastapi import FastAPI
from app.chatbot_router import router as chatbot_router
import uvicorn
import os

app = FastAPI(
    title="Chatbot Resume Filter",
    description="API for chatbot-driven CV filtering",
    version="1.0.0"
)

# Register router
app.include_router(chatbot_router, prefix="/chatbot")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # Default port only for local
    uvicorn.run("main:app", host="0.0.0.0", port=port)
