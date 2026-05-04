# Cloud Cover Classification — ML Inference System

Production-grade machine learning service for predicting weather conditions from environmental parameters.
Exposed via a REST API and an interactive client, with a unified preprocessing + model pipeline to ensure consistent inference.

---

## Live Demo

* **App**: https://cloud-cover-classification-cm3ajlcsp6ytwzkdphchzy.streamlit.app/

<details>
<summary>API (for technical review)</summary>

* https://cloud-cover-api.onrender.com
* https://cloud-cover-api.onrender.com/docs

</details>

---

## System Architecture

```
Client (Streamlit)
        ↓
POST /predict
        ↓
FastAPI Service
        ↓
scikit-learn Pipeline
(preprocessing + model)
        ↓
Prediction + Confidence
```

---

## API Contract

### Endpoint

```
POST /predict
```

### Request

```json
{
  "Temperature": 14.0,
  "Humidity": 73,
  "Wind_Speed": 9.5,
  "Precipitation": 82.0,
  "Cloud_Cover": "partly cloudy",
  "Atmospheric_Pressure": 1010.82,
  "UV_Index": 2,
  "Visibility": 3.5,
  "Season": "Winter",
  "Location": "inland"
}
```

### Response

```json
{
  "prediction": "Rainy",
  "confidence": 0.87
}
```

---

## Tech Stack

* **ML**: scikit-learn (Pipeline, ColumnTransformer)
* **API**: FastAPI, Uvicorn
* **Client**: Streamlit
* **Data**: pandas
* **Deployment**: Render, Streamlit Cloud

---

## Local Setup

```bash
git clone https://github.com/YuvarajGML/Cloud-Cover-Classification.git
cd Cloud-Cover-Classification
pip install -r requirements.txt
```

### Run API

```bash
uvicorn backend.app:app --reload
```

### Run Client

```bash
streamlit run frontend/streamlit_app.py
```

---

## Repository Structure

```
Cloud-Cover-Classification/
│
├── backend/
│   ├── app.py
│   └── model_pipeline.pkl
│
├── frontend/
│   └── streamlit_app.py
│
├── requirements.txt
└── README.md
```

---

## Engineering Notes

* Single pipeline artifact ensures consistent preprocessing and inference
* Input validation enforced via FastAPI + Pydantic
* Stateless inference service design

---

## Author

Yuvaraj Gopi
