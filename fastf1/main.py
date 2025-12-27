from fastapi import FastAPI
from fastf1.database.base import Base
from fastf1.database.session import engine
from fastf1.api.router import api_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="FastAPI Starter")
app.include_router(api_router)

@app.get("/")
def root():
    return {"message": "FastAPI Starter Template Running!"}

@app.get("/health")
def health():
    return {"status": "healthy"}