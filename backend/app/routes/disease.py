import os
import joblib
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
model_path = os.path.join(BASE_DIR, "disease_model.pkl")

model, vectorizer = joblib.load(model_path)

class DiseaseInput(BaseModel):
    text: str

@router.post("/predict-disease")
def predict_disease(data: DiseaseInput):
    input_vector = vectorizer.transform([data.text])
    prediction = model.predict(input_vector)
    return {"prediction": prediction[0]}