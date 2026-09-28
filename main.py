from fastapi import FastAPI
from app.routes import router

# Add title and description here:
app = FastAPI(
    title="FitBuddy API",
    description="Backend API for FitBuddy Fitness Application",
    version="1.0.0"
)

app.include_router(router)
