from fastapi import APIRouter
import os
import joblib

router = APIRouter()

# Go back from routes -> app
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Commented temporarily
# model_path = os.path.join(BASE_DIR, "model.pkl")
# print("Loading model from:", model_path)
# model = joblib.load(model_path)

@router.get("/price-test")
def test():
    return {"message": "Market route working"}