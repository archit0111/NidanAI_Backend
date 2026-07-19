from pydantic import BaseModel
from typing import List


class Prediction(BaseModel):
    disease: str
    confidence: float


class ReportResponse(BaseModel):
    query: str
    symptoms: List[str]
    predictions: List[Prediction]
    medical_report: str