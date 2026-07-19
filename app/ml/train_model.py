import pandas as pd
from pathlib import Path

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib

BASE_DIR = Path(__file__).resolve().parent.parent
DATASET = BASE_DIR / "datasets" / "Diseases_and_Symptoms_dataset.csv"

df = pd.read_csv(DATASET)

# Features
X = df.drop(columns=["diseases"])

# Labels
y = df["diseases"]

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print("Training model...")

model = RandomForestClassifier(
    n_estimators=50,
    max_depth=20,
    random_state=42,
    n_jobs=-1
)

model.fit(X_train, y_train)

pred = model.predict(X_test)

acc = accuracy_score(y_test, pred)

print(f"Accuracy : {acc:.4f}")

SAVE_DIR = BASE_DIR / "ml" / "saved_models"
SAVE_DIR.mkdir(exist_ok=True)

joblib.dump(model, SAVE_DIR / "disease_model.pkl")
joblib.dump(X.columns.tolist(), SAVE_DIR / "symptom_columns.pkl")

print("Model saved successfully.")