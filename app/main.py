from fastapi import FastAPI
from app.chatbot_router import router as chatbot_router
from app.router.ml_router import router as ml_router  # ← NEW Import
import uvicorn
import os

app = FastAPI(
    title="Chatbot Resume Filter",
    description="API for chatbot-driven CV filtering + ML Resume Classifier",
    version="1.0.0"
)

# Register routers
app.include_router(chatbot_router, prefix="/chatbot")
app.include_router(ml_router, prefix="/ml")  # ← ML Model API Routes

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # Default port only for local
    uvicorn.run("main:app", host="0.0.0.0", port=port)
