from fastapi import FastAPI
from app.routes.weather import router as weather_router
from app.routes.disease import router as disease_router
from app.routes.crop import router as crop_router
from app.routes.market_routes import router as market_router
from app.routes.users import router as user_router

app = FastAPI()

app.include_router(weather_router)
app.include_router(disease_router)
app.include_router(crop_router)
app.include_router(market_router)
app.include_router(user_router)