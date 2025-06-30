from pydantic import BaseModel
from typing import List, Optional

class CustomerFeatures(BaseModel):
    Recency: float
    Frequency: float
    Monetary: float

class PredictionResponse(BaseModel):
    risk_probability: float
