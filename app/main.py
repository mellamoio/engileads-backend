from fastapi import FastAPI
from app.routes import api_router
from app.db.base import Base
from app.db.session import engine

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Contact Backend API",
    version="1.0.0"
)

app.include_router(api_router,prefix="/api/v1")

@app.get("/")
def health_check():
    return {"status": "API running"}