import pandas as pd
from pathlib import Path

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

from sklearn.ensemble import (
    RandomForestClassifier,
    ExtraTreesClassifier
)

BASE_DIR = Path(__file__).resolve().parent.parent
DATASET = BASE_DIR / "datasets" / "Diseases_and_Symptoms_dataset.csv"

print("Loading dataset...")

df = pd.read_csv(DATASET)

X = df.drop(columns=["diseases"])
y = df["diseases"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

models = {
    "Random Forest": RandomForestClassifier(
        n_estimators=300,
        random_state=42,
        n_jobs=-1,
    ),
    "Extra Trees": ExtraTreesClassifier(
        n_estimators=300,
        random_state=42,
        n_jobs=-1,
    )
}

results = []

for name, model in models.items():

    print(f"\nTraining {name}...")

    model.fit(X_train, y_train)

    pred = model.predict(X_test)

    acc = accuracy_score(y_test, pred)

    results.append((name, acc))

print("\n=============================")

for name, acc in sorted(results, key=lambda x: x[1], reverse=True):
    print(f"{name:20} {acc:.4f}")
