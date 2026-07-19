from app.llm.gemini import generate_response
import json


class SymptomExtractor:

    def extract(self, text: str):

        prompt = f"""
Extract only the symptoms from the user's message.

Rules:
- Return ONLY a JSON array.
- Convert symptoms to lowercase.
- Remove duplicates.
- Do not explain anything.

Example:

Input:
I have fever, cough and headache.

Output:
["fever","cough","headache"]

User:

{text}
"""

        response = generate_response(prompt)

        try:
            symptoms = json.loads(response)
            return symptoms

        except Exception:
            return []