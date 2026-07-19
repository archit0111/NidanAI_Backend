from app.rag.knowledge_base import MedicalKnowledgeBase


class KnowledgeService:

    def __init__(self):
        self.db = MedicalKnowledgeBase()

    def get_disease_information(self, disease: str):

        disease = disease.strip().lower()

        row = self.db.data[
            self.db.data["Disease"] == disease
        ]

        if row.empty:
            return None

        row = row.iloc[0]

        return {
            "disease": row["Disease"],
            "description": row["Description"],
            "diet": row["Diet"],
            "medication": row["Medication"],
            "precautions": [
                row["Precaution_1"],
                row["Precaution_2"],
                row["Precaution_3"],
                row["Precaution_4"],
            ],
            "workouts": row["Workouts"],
        }