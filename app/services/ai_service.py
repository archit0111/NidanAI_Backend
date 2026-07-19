import json
import re

from app.ml.predictor import predict_disease
from app.llm.gemini import GeminiClient
from app.llm.prompt_builder import MedicalPromptBuilder


class AIService:

    def __init__(self):
        self.gemini = GeminiClient()
        self.prompt_builder = MedicalPromptBuilder()

    def clean_json(self, text):
        text = re.sub(r"```json|```", "", text)
        return text.strip()

    def generate_report(self, patient_data):

        predictions = predict_disease(
            patient_data["symptoms"]
        )

        prompt = self.prompt_builder.build(
            patient_data,
            predictions
        )

        response = self.gemini.generate(prompt)

        response = self.clean_json(response)

        report = json.loads(response)

        report["mlPrediction"] = predictions

        return report