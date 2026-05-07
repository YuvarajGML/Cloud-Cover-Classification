from fastapi import FastAPI
from pydantic import BaseModel
from typing import Literal
import pickle
import os
import pandas as pd
import numpy as np

app = FastAPI()

# ✅ Load artifacts bundle (ONLY load, never overwrite here)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "weather_model_bundle.pkl")

with open(MODEL_PATH, "rb") as f:
    artifacts = pickle.load(f)

# ✅ Extract all components
model = artifacts["model"]
scaler = artifacts["scaler"]
encoder = artifacts["encoder"]
num_cols = artifacts["num_cols"]
cat_cols = artifacts["cat_cols"]
encoded_cols = artifacts["encoded_cols"]


# ✅ Clean input schema
class UserIP(BaseModel):
    Temperature: float
    Humidity: float
    Wind_Speed: float
    Precipitation: float
    Atmospheric_Pressure: float
    Visibility: float
    Season: Literal["Autumn", "Spring", "Summer", "Winter"]
    Location: Literal["coastal", "inland", "mountain"]


# ✅ Health check endpoint
@app.get("/")
def root():
    return {"message": "Cloud Cover Prediction API is running 🚀"}


# ✅ Prediction endpoint
@app.post("/predict")
def predict(user_input: UserIP):
    try:
        # 🔹 Convert input to raw dataframe
        input_dict = {
            "Temperature": user_input.Temperature,
            "Humidity": user_input.Humidity,
            "Wind Speed": user_input.Wind_Speed,
            "Precipitation (%)": user_input.Precipitation,
            "Atmospheric Pressure": user_input.Atmospheric_Pressure,
            "Visibility (km)": user_input.Visibility,
            "Season": user_input.Season,
            "Location": user_input.Location
        }

        raw_data = pd.DataFrame([input_dict])

        # 🔹 Scale numerical features
        raw_data[num_cols] = scaler.transform(raw_data[num_cols])

        # 🔹 One-hot encode categorical features
        encoded_data = encoder.transform(raw_data[cat_cols])

        encoded_df = pd.DataFrame(
            encoded_data,
            columns=encoded_cols
        )

        # 🔹 Combine final features
        X_api = pd.concat(
            [raw_data[num_cols], encoded_df],
            axis=1
        )

        # 🔹 Prediction
        prediction = model.predict(X_api)[0]

        # 🔹 Confidence (optional but powerful)
        confidence = None
        if hasattr(model, "predict_proba"):
            confidence = np.max(model.predict_proba(X_api)[0])

        # ✅ Clean response
        return {
            "prediction": str(prediction),
            "confidence": round(float(confidence), 4) if confidence else None
        }

    except Exception as e:
        return {"error": str(e)}