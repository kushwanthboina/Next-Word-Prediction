import pickle

class NGramPredictor:
    def __init__(self, model_path):
        """Load the trained model."""
        with open(model_path, "rb") as f:
            self.model = pickle.load(f)
        print(f"Model loaded with {len(self.model)} N-grams.")  # Debugging

    def predict(self, context):
        """Predict the next word given a context."""
        tokens = context.lower().strip().split()  # Normalize and tokenize input
        print(f"Tokens from input: {tokens}")  # Debugging

        # Extract the last two words (bigram context) from the input
        context_tuple = tuple(tokens[-2:])
        print(f"Generated context tuple: {context_tuple}")  # Debugging

        # Retrieve prediction
        predictions = self.model.get(context_tuple)
        if predictions:
            print(f"Predictions for context {context_tuple}: {predictions}")  # Debugging
            return predictions[0]  # Return the first prediction
        else:
            print(f"No predictions for context: {context_tuple}")  # Debugging
            return "No prediction available"
