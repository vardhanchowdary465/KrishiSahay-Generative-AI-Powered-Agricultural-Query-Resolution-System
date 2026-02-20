from fastapi import FastAPI
from app.routes import query

app = FastAPI(title="KrishiSahay API")

app.include_router(query.router, prefix="/query", tags=["Query"])

@app.get("/")
def root():
    return {"message": "KrishiSahay Backend Running"}