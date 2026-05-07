# WeatherIQ — ML Inference System

WeatherIQ is a machine learning inference system for classifying weather conditions from environmental parameters.

The project focuses on deploying machine learning models through a modular inference architecture with:
- API-based model serving
- reproducible preprocessing pipelines
- frontend/backend integration
- containerized deployment
- real-time prediction workflows

The platform exposes a FastAPI inference service alongside an interactive Streamlit frontend for live predictions.

---

# Live Demo

## Frontend Application

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
- Request validation using Pydantic schemas
- Unified preprocessing and inference workflow
- Serialized ML artifact bundle for reproducible inference
- Probability-based confidence estimation
- Decoupled frontend and backend services
- Containerized deployment using Docker and Docker Compose
- Modular deployment-ready project structure

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

The backend loads a serialized artifact bundle containing:
- trained classification model
- feature scaler
- one-hot encoder
- feature mappings

This ensures preprocessing consistency between training and inference environments while reducing feature mismatch during deployment.

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

## Build Containers

```bash
docker compose build
```

## Run Services

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
uvicorn app:app --reload --port 10000
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
│   ├── Dockerfile
│   └── weather_model_bundle.pkl
│
├── Frontend/
│   ├── frontend.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── docker-compose.yml
├── .dockerignore
└── README.md
```

---

# Author

## Yuvaraj Gopi
