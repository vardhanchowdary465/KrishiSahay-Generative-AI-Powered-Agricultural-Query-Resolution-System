from fastapi import APIRouter

router = APIRouter()

@router.post("/predict-crop")
def predict_crop(n: float, p: float, k: float, ph: float):
    
    if ph > 7:
        return {"recommended_crop": "Wheat"}
    
    return {"recommended_crop": "Rice"}