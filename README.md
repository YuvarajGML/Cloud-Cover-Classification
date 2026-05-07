# WeatherIQ — Cloud Cover Prediction System

Production-grade machine learning inference system for predicting weather conditions from environmental parameters using a unified preprocessing and classification pipeline.

The platform combines:
- a FastAPI backend inference service
- an interactive Streamlit frontend
- Dockerized deployment architecture
- reproducible machine learning inference workflows

---

## Live Demo

### Frontend Application
🌐 https://cloud-cover-classification-cm3ajlcsp6ytwzkdphchzy.streamlit.app/

<details>
<summary><strong>Backend API & Technical Documentation</strong></summary>

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
│  ML Inference Stack  │
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

# Features

- RESTful machine learning inference API
- Interactive Streamlit prediction dashboard
- Confidence score estimation
- Unified preprocessing + inference workflow
- Dockerized multi-service architecture
- FastAPI schema validation using Pydantic
- Reproducible deployment environment
- Production-oriented backend design
- Modular frontend/backend separation

---

# API Contract

## Endpoint

```http
POST /predict
```

---

## Request Body

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

## Response

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
- numerical feature mappings
- encoded categorical feature mappings

This architecture ensures preprocessing consistency across:
- training
- validation
- production inference

---

# Tech Stack

| Layer | Technology |
|---|---|
| Machine Learning | scikit-learn 1.6.1 |
| Backend API | FastAPI, Uvicorn |
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

---

## Run Application

```bash
docker compose up
```

---

## Available Services

| Service | URL |
|---|---|
| Frontend | http://localhost:8501 |
| Backend API | http://localhost:10000 |
| Swagger Docs | http://localhost:10000/docs |

---

# Local Development Setup

## Clone Repository

```bash
git clone https://github.com/YuvarajGML/Cloud-Cover-Classification.git
cd Cloud-Cover-Classification
```

---

## Backend Setup

```bash
cd backend
pip install -r requirements.txt
uvicorn app:app --reload
```

---

## Frontend Setup

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
│   ├── Dockerfile
│   ├── requirements.txt
│   └── weather_model_bundle.pkl
│
├── Frontend/
│   ├── frontend.py
│   ├── Dockerfile
│   └── requirements.txt
│
├── docker-compose.yml
└── README.md
```

---

# Docker Images

- Backend: `pridesage32/weather-backend`
- Frontend: `pridesage32/weather-frontend`

---

# Engineering Notes

- Stateless inference service design
- Unified preprocessing and inference pipeline
- Strict schema validation via FastAPI + Pydantic
- Decoupled frontend/backend architecture
- Reproducible containerized deployment environment

---

# Future Improvements

- CI/CD pipeline integration
- Kubernetes deployment
- Model monitoring and logging
- GPU-backed inference support
- Authentication and rate limiting
- Automated retraining workflow

---

# Author

## Yuvaraj Gopi
