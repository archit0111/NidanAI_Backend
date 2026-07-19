from app.llm.gemini import generate_response

print("Testing Gemini...")

response = generate_response(
    "Say hello in one sentence."
)

print(response)