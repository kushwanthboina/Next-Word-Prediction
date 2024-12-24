from fastapi import FastAPI
from app.routes import router

app = FastAPI()

# Include the routes for prediction
app.include_router(router)

@app.get("/")
async def root():
    return {"message": "Welcome to the Next Word Prediction API"}
