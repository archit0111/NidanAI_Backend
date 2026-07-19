import json
import re

from app.rag.retriever import MedicalRetriever
from app.rag.prompt_builder import MedicalPromptBuilder
from app.llm.gemini import GeminiClient


class AIService:

    def __init__(self):

        self.retriever = MedicalRetriever()
        self.prompt_builder = MedicalPromptBuilder()
        self.gemini = GeminiClient()


    def clean_json(self, response):

        response = response.strip()

        response = re.sub(
            r"```json|```",
            "",
            response
        )

        return response.strip()


    def generate_report(self, patient_data):

        query = f"""
        Symptoms:
        {patient_data.get("symptoms")}

        Description:
        {patient_data.get("description")}
        """


        knowledge = self.retriever.search(
            query,
            top_k=5
        )


        prompt = self.prompt_builder.build(
            patient_data,
            knowledge
        )


        response = self.gemini.generate(
            prompt
        )


        cleaned = self.clean_json(
            response
        )


        try:

            report = json.loads(
                cleaned
            )


        except json.JSONDecodeError:

            return {
                "error": "AI returned invalid JSON",
                "raw": response
            }


        return report   # IMPORTANT