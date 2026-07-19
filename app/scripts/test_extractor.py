from app.ml.symptom_extractor import SymptomExtractor

extractor = SymptomExtractor()

symptoms = extractor.extract(
    "I have fever, headache and cough for three days."
)

print(symptoms)
