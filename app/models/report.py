from datetime import datetime
from pydantic import BaseModel, Field
from typing import List, Optional


class MedicalReport(BaseModel):

    user_id: Optional[str] = None

    age: int

    symptoms: List[str]

    description: str

    ai_report: dict

    created_at: datetime = Field(
        default_factory=datetime.utcnow
    )