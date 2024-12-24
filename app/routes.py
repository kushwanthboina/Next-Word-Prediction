from fastapi import APIRouter, Query
from model.predict import NGramPredictor

# Create an APIRouter instance
router = APIRouter()

# Initialize the predictor
predictor = NGramPredictor("model/next_word_model.pkl")

@router.get("/predict")
def predict_next_word(context: str = Query(..., description="Context words for prediction")):
    """API endpoint to predict the next word."""
    next_word = predictor.predict(context)
    return {"context": context, "next_word": next_word}
