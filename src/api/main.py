from fastapi import FastAPI
from src.api.pydantic_models import CustomerFeatures, PredictionResponse
import mlflow.pyfunc
import pandas as pd

app = FastAPI()

# Load model from MLflow registry
model_uri = "models:/credit-risk-model/Production"  # make sure you registered it
model = mlflow.pyfunc.load_model(model_uri)


@app.get("/")
def read_root():
    return {"message": "Credit Risk Scoring API is live!"}


@app.post("/predict", response_model=PredictionResponse)
def predict_risk(data: CustomerFeatures):
    input_df = pd.DataFrame([data.dict()])
    prob = model.predict(input_df)[0]
    return PredictionResponse(risk_probability=round(float(prob), 4))
