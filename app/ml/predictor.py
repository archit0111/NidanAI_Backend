import joblib
import numpy as np

MODEL = joblib.load("app/ml/saved_models/disease_model.pkl")
COLUMNS = joblib.load("app/ml/saved_models/symptom_columns.pkl")


def predict_disease(symptoms):

    x = np.zeros(len(COLUMNS))

    symptoms = [s.lower().strip() for s in symptoms]

    for i, symptom in enumerate(COLUMNS):
        if symptom.lower() in symptoms:
            x[i] = 1

    probs = MODEL.predict_proba([x])[0]

    top = probs.argsort()[-3:][::-1]

    return [
        {
            "disease": MODEL.classes_[i],
            "confidence": round(float(probs[i]), 3)
        }
        for i in top
    ]