from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field, field_validator
from typing import Literal
import pickle
import os
import pandas as pd

app = FastAPI()

# ✅ Load model
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "model_pipeline.pkl")

with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)


# ✅ Input schema with validation
class UserIP(BaseModel):
    Temperature: float = Field(..., ge=-50, le=60)
    Humidity: float = Field(..., ge=0, le=100)
    Wind_Speed: float = Field(..., ge=0, le=150)
    Precipitation: float = Field(..., ge=0, le=100)
    Cloud_Cover: str
    Atmospheric_Pressure: float = Field(..., ge=800, le=1100)
    UV_Index: float = Field(..., ge=0, le=15)
    Visibility: float = Field(..., ge=0, le=20)
    Season: Literal["Autumn", "Spring", "Summer", "Winter"]
    Location: Literal["coastal", "inland", "mountain"]

    # 🔹 Normalize Cloud Cover values
    @field_validator("Cloud_Cover")
    @classmethod
    def validate_cloud_cover(cls, v):
        allowed = {
            "clear",
            "partly cloudy",
            "cloudy",
            "overcast"
        }
        v_clean = v.strip().lower()
        if v_clean not in allowed:
            raise ValueError(f"Cloud_Cover must be one of {allowed}")
        return v_clean


# ✅ Health check
@app.get("/")
def root():
    return {"message": "Weather Prediction API is running 🚀"}


# ✅ Prediction endpoint
@app.post("/predict")
def predict(user_input: UserIP):
    try:
        # 🔹 Map to training feature names
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

        # 🔹 Model prediction
        prediction = model.predict(input_df)[0]

        # 🔹 Confidence
        confidence = None
        if hasattr(model, "predict_proba"):
            probs = model.predict_proba(input_df)[0]
            confidence = float(max(probs))

        return {
            "prediction": str(prediction),
            "confidence": round(confidence, 4) if confidence is not None else None
        }

    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Inference error: {str(e)}")
