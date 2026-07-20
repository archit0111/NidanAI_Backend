import os
import time
from dotenv import load_dotenv
from google import genai
from google.genai.errors import APIError

load_dotenv()

class GeminiClient:

    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("GEMINI_API_KEY missing in .env")
        self.client = genai.Client(api_key=api_key)

    def generate(self, prompt, response_schema=None):
        config = None
        if response_schema:
            from google.genai import types
            config = types.GenerateContentConfig(
                response_mime_type="application/json",
                response_schema=response_schema,
                temperature=0.2,
            )

        # Fallback list of models in case of 503 or overload errors
        models = ["gemini-2.5-flash", "gemini-1.5-flash"]
        last_error = None

        for model in models:
            for attempt in range(2):  # Try each model up to 2 times
                try:
                    response = self.client.models.generate_content(
                        model=model,
                        contents=prompt,
                        config=config
                    )
                    return response.text
                except Exception as e:
                    last_error = e
                    # If it's a rate limit or overloaded error, wait slightly and retry
                    time.sleep(1.0)
        
        # If all else fails, raise the last exception
        raise last_error if last_error else RuntimeError("Gemini API call failed with no error context")