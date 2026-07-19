class MedicalPromptBuilder:

    def build(
        self,
        patient_data,
        knowledge
    ):

        context = "\n\n".join(
            knowledge
        )


        prompt = f"""
You are an AI healthcare assistant.

Your task is to analyze patient symptoms and provide a professional medical guidance report.

IMPORTANT:
- Do not give a final diagnosis.
- Provide possible conditions only.
- Recommend consulting a qualified doctor.
- Use only the provided medical knowledge context.

PATIENT INFORMATION:

{patient_data}


MEDICAL KNOWLEDGE CONTEXT:

{context}


Generate a structured response in JSON format:

{{
    "possibleDisease": [],
    "confidence": "",
    "severity": "",
    "description": "",
    "recommendations": [],
    "medications": [],
    "tests": [],
    "diet": [],
    "workout": [],
    "precautions": [],
    "emergency": false
}}

Return only valid JSON.
"""

        return prompt
    