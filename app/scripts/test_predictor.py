from app.ml.predictor import DiseasePredictor

predictor = DiseasePredictor()

result = predictor.predict(
    [
        "fever",
        "headache",
        "cough"
    ]
)

for disease in result:
    print(disease)