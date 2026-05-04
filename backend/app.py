from fastapi import FastAPI
from pydantic import BaseModel
from typing import Literal
import pickle
import os
import pandas as pd

app = FastAPI()

# ✅ Load model (ONLY load, never overwrite here)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "model_pipeline.pkl")

with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)


# ✅ Clean input schema (ONLY features, no target)
class UserIP(BaseModel):
    Temperature: float
    Humidity: float
    Wind_Speed: float
    Precipitation: float
    Cloud_Cover: str   # categorical
    Atmospheric_Pressure: float
    UV_Index: float
    Visibility: float
    Season: Literal["Autumn", "Spring", "Summer", "Winter"]
    Location: Literal["coastal", "inland", "mountain"]


# ✅ Health check endpoint
@app.get("/")
def root():
    return {"message": "Weather Prediction API is running 🚀"}


# ✅ Prediction endpoint
@app.post("/predict")
def predict(user_input: UserIP):
    try:
        # 🔹 Convert input to model-compatible format
        input_dict = {
            "Temperature": user_input.Temperature,
            "Humidity": user_input.Humidity,
            "Wind Speed": user_input.Wind_Speed,
            "Precipitation (%)": user_input.Precipitation,
            "Cloud Cover": user_input.Cloud_Cover,
            "Atmospheric Pressure": user_input.Atmospheric_Pressure,
            "UV Index": user_input.UV_Index,
            "Visibility (km)": user_input.Visibility,
            "Season": user_input.Season,
            "Location": user_input.Location
        }

        input_df = pd.DataFrame([input_dict])

        # 🔹 Prediction
        prediction = model.predict(input_df)[0]

        # 🔹 Confidence (optional but powerful)
        confidence = None
        if hasattr(model, "predict_proba"):
            confidence = max(model.predict_proba(input_df)[0])

        # ✅ Return clean response (NO int casting!)
        return {
            "prediction": prediction,
            "confidence": round(float(confidence), 4) if confidence else None
        }

    except Exception as e:
        return {"error": str(e)}
