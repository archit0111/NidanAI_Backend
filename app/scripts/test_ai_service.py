from app.services.ai_service import AIService


service = AIService()


patient = {

    "age": 25,

    "symptoms": [
        "cough",
        "breathing difficulty",
        "chest tightness"
    ],

    "description":
    "Symptoms started 3 days ago"

}


report = service.generate_report(
    patient
)


print(report)

print()

print(
    report["possibleDisease"]
)