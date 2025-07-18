from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
import joblib
from app.ml_model.model_testing import ResumeClassifier  # Update path based on your structure

router = APIRouter()

# Load model artifacts once at startup
model = joblib.load("app/ml_model/Resume_Ensemble_Model.pkl")
vectorizer = joblib.load("app/ml_model/Resume_Tfidf_Vectorizer.pkl")
label_encoder = joblib.load("app/ml_model/Resume_LabelEncoder.pkl")

@router.post("/predict")
async def predict(request: Request):
    data = await request.json()

    if not data or "text" not in data:
        return JSONResponse(content={"error": "No text provided"}, status_code=400)

    cleaned = ResumeClassifier.clean_text(data["text"])
    features = vectorizer.transform([cleaned])
    prediction = model.predict(features)
    label = label_encoder.inverse_transform(prediction)[0]

    return {"category": label}

@router.get("/")
async def home():
    return {"message": "Resume Classifier API is running."}
