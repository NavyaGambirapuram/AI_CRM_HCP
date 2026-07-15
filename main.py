
from fastapi import FastAPI
from dotenv import load_dotenv
from routers import interactions
from database import engine
from models import Base
import os

load_dotenv()

app = FastAPI(title="AI_CRM_HCP")

Base.metadata.create_all(bind=engine)

app.include_router(interactions.router,
                   prefix="/interactions",
                   tags=["Interactions"])

@app.get("/")
def home():
    return {"message": "Welcome to AI_CRM_HCP API!"}


