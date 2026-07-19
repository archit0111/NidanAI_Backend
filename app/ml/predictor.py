import os
import pickle

MODEL_PATH = "app/ml/saved_models/disease_model.pkl"
SYMPTOM_PATH = "app/ml/saved_models/symptom_columns.pkl"

if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(
        "Model not found. Run download_model.py first."
    )

with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

with open(SYMPTOM_PATH, "rb") as f:
    symptom_columns = pickle.load(f)