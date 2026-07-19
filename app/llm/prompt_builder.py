class MedicalPromptBuilder:

    def build(self, patient, predictions):

        return f"""
You are an expert physician.

Patient Information

Age:
{patient.get("age")}

Symptoms:
{patient.get("symptoms")}

Description:
{patient.get("description")}

Possible diseases predicted by ML:

{predictions}

Generate ONLY valid JSON with the following fields:

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
"""