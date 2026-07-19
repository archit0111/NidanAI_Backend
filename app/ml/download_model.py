import os
from huggingface_hub import hf_hub_download

MODEL_DIR = "app/ml/saved_models"
os.makedirs(MODEL_DIR, exist_ok=True)

REPO_ID = "Archit011/nidana-disease-model"

FILES = [
    "disease_model.pkl",
    "symptom_columns.pkl",
]

for file in FILES:
    path = hf_hub_download(
        repo_id=REPO_ID,
        filename=file,
        local_dir=MODEL_DIR,
        token=os.getenv("HF_TOKEN"),
    )
    print(f"Downloaded: {path}")
    