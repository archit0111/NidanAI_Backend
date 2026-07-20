import json
from pydantic import BaseModel, Field
from typing import List

from app.ml.predictor import predict_disease
from app.llm.gemini import GeminiClient
from app.llm.prompt_builder import MedicalPromptBuilder


class MedicalReportSchema(BaseModel):
    possibleDisease: List[str] = Field(description="Possible diseases matching the symptoms")
    confidence: str = Field(description="Confidence level (e.g. High, Moderate, Low)")
    severity: str = Field(description="Severity (e.g. Mild, Moderate, Severe)")
    description: str = Field(description="Clinical description of the assessment")
    recommendations: List[str] = Field(default_factory=list, description="General health advice")
    medications: List[str] = Field(default_factory=list, description="Suggested medications to discuss with a doctor")
    tests: List[str] = Field(default_factory=list, description="Recommended medical diagnostic tests")
    diet: List[str] = Field(default_factory=list, description="Dietary suggestions")
    workout: List[str] = Field(default_factory=list, description="Exercise and lifestyle plans")
    precautions: List[str] = Field(default_factory=list, description="Safety precautions")
    emergency: bool = Field(default=False, description="Whether this calls for immediate emergency attention")


class AIService:

    def __init__(self):
        self.gemini = GeminiClient()
        self.prompt_builder = MedicalPromptBuilder()

    def generate_report(self, patient_data):
        # 1. Run local ML model predictions (instant)
        predictions = predict_disease(
            patient_data["symptoms"]
        )

        # 2. Build instructions prompt
        prompt = self.prompt_builder.build(
            patient_data,
            predictions
        )

        # 3. Call Gemini with Pydantic structured schema (reduces latency significantly)
        response_text = self.gemini.generate(prompt, response_schema=MedicalReportSchema)

        # 4. Parse JSON
        report = json.loads(response_text)

        # 5. Append predictions data
        report["mlPrediction"] = predictions

        return report