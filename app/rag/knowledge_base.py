import pandas as pd
from app.rag.loader import DatasetLoader


class MedicalKnowledgeBase:

    def __init__(self):
        loader = DatasetLoader()

        self.description = loader.description.copy()
        self.diets = loader.diets.copy()
        self.medications = loader.medications.copy()
        self.precautions = loader.precautions.copy()
        self.workout = loader.workout.copy()

        self.prepare()

    def normalize(self, text):
        return str(text).strip().lower()

    def prepare(self):

        datasets = [
            self.description,
            self.diets,
            self.medications,
            self.precautions,
            self.workout
        ]

        for df in datasets:
            df["Disease"] = df["Disease"].apply(self.normalize)

    def build(self):

        knowledge = self.description.copy()

        knowledge = knowledge.merge(
            self.diets,
            on="Disease",
            how="left"
        )

        knowledge = knowledge.merge(
            self.medications,
            on="Disease",
            how="left"
        )

        knowledge = knowledge.merge(
            self.precautions,
            on="Disease",
            how="left"
        )

        knowledge = knowledge.merge(
            self.workout,
            on="Disease",
            how="left"
        )

        return knowledge


if __name__ == "__main__":

    kb = MedicalKnowledgeBase()

    knowledge = kb.build()

    knowledge.to_json(
        "app/datasets/medical_knowledge.json",
        orient="records",
        indent=4
    )

    print("✅ Medical Knowledge Base Created Successfully")
    print(f"Total Diseases: {len(knowledge)}")

    kb = MedicalKnowledgeBase()

    knowledge = kb.build()

    print(knowledge.head())

    print()

    print(knowledge.columns)