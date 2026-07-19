import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATASET_DIR = BASE_DIR / "datasets"


class DatasetLoader:

    def __init__(self):
        self.description = pd.read_csv(DATASET_DIR / "description.csv")
        self.diets = pd.read_csv(DATASET_DIR / "diets.csv")
        self.medications = pd.read_csv(DATASET_DIR / "medications.csv")
        self.precautions = pd.read_csv(DATASET_DIR / "precautions.csv")
        self.workout = pd.read_csv(DATASET_DIR / "workout.csv")
        self.symptoms = pd.read_csv(DATASET_DIR / "Diseases_and_Symptoms_dataset.csv")


if __name__ == "__main__":

    loader = DatasetLoader()

    print(loader.description.head())
    print(loader.diets.head())
    print(loader.medications.head())
    print(loader.precautions.head())
    print(loader.workout.head())
    print(loader.symptoms.head())