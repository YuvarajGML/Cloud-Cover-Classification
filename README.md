# WeatherIQ — Production ML Inference Platform

WeatherIQ is a production-oriented machine learning system for weather condition classification based on environmental parameters.

The project focuses on the engineering aspects of deploying machine learning models into real-world inference systems, including:
- API-based model serving
- reproducible preprocessing pipelines
- frontend/backend integration
- containerized deployment
- modular system design

The platform exposes a FastAPI inference service alongside an interactive Streamlit client for real-time predictions.

---

## Live Demo

### Frontend Application
🌐 https://cloud-cover-classification-cm3ajlcsp6ytwzkdphchzy.streamlit.app/

<details>
<summary><strong>Backend API & Documentation</strong></summary>

### API Base URL
https://cloud-cover-api.onrender.com

### Swagger Documentation
https://cloud-cover-api.onrender.com/docs

</details>

---

# System Architecture

```text
┌──────────────────────┐
│   Streamlit Client   │
└──────────┬───────────┘
           │
           ▼
     POST /predict
           │
           ▼
┌──────────────────────┐
│    FastAPI Backend   │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│  ML Inference Layer  │
│                      │
│ • Feature Scaling    │
│ • One-Hot Encoding   │
│ • Classification     │
└──────────┬───────────┘
           │
           ▼
 Prediction + Confidence
```

---

# Engineering Highlights

- RESTful inference API using FastAPI
- Structured request validation with Pydantic
- Unified preprocessing and inference workflow
- Serialized ML artifact pipeline for reproducible inference
- Confidence score estimation using probability outputs
- Decoupled frontend and backend architecture
- Containerized deployment using Docker and Docker Compose
- Production-style service orchestration

---

# API Contract

## Endpoint

```http
POST /predict
```

---

## Request Example

```json
{
  "Temperature": 14.0,
  "Humidity": 73,
  "Wind_Speed": 9.5,
  "Precipitation": 82.0,
  "Atmospheric_Pressure": 1010.82,
  "Visibility": 3.5,
  "Season": "Winter",
  "Location": "inland"
}
```

---

## Response Example

```json
{
  "prediction": "Rainy",
  "confidence": 0.87
}
```

---

# ML Inference Pipeline

The backend uses a serialized artifact bundle containing:
- trained classification model
- feature scaler
- one-hot encoder
- feature mappings

This ensures preprocessing consistency between training and production inference while reducing feature drift and inference mismatch.

---

# Technology Stack

| Layer | Technologies |
|---|---|
| Machine Learning | scikit-learn |
| Backend | FastAPI, Uvicorn |
| Frontend | Streamlit |
| Data Processing | pandas, NumPy |
| Containerization | Docker, Docker Compose |
| Deployment | Render, Streamlit Cloud |

---

# Dockerized Deployment

## Build Services

```bash
docker compose build
```

## Run Application

```bash
docker compose up
```

---

# Local Development

## Clone Repository

```bash
git clone https://github.com/YuvarajGML/Cloud-Cover-Classification.git
cd Cloud-Cover-Classification
```

---

## Start Backend

```bash
cd backend
pip install -r requirements.txt
uvicorn app:app --reload
```

---

## Start Frontend

```bash
cd Frontend
pip install -r requirements.txt
streamlit run frontend.py
```

---

# Repository Structure

```text
Cloud-Cover-Classification/
│
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   └── weather_model_bundle.pkl
│
├── Frontend/
│   ├── frontend.py
│   └── requirements.txt
│
├── docker-compose.yml
└── README.md
```

---

# Author

## Yuvaraj Gopi
