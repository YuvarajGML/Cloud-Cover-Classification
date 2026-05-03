# 🌦️ Weather Prediction ML App

A full-stack machine learning application that predicts weather conditions based on environmental parameters.
Built using **FastAPI (backend)**, **Streamlit (frontend)**, and a **scikit-learn pipeline** for robust inference.

---

## 🚀 Features

* Predict weather type (Rainy, Clear, Cloudy, etc.)
* End-to-end ML pipeline (no manual preprocessing required)
* FastAPI backend for scalable inference
* Streamlit frontend with clean UI
* Confidence score for predictions

---

## 🧠 Tech Stack

* **Machine Learning**: scikit-learn (Pipeline)
* **Backend**: FastAPI + Uvicorn
* **Frontend**: Streamlit
* **Data Processing**: pandas

---

## 📂 Project Structure

```id="a9x2ke"
weather-ml-app/
│
├── backend/
│   ├── fastapi_app.py
│   ├── model_pipeline.pkl
│
├── frontend/
│   ├── streamlit_app.py
│
├── requirements.txt
├── README.md
```

---

## ⚙️ How It Works

```id="1q3m9p"
User Input (Streamlit UI)
        ↓
POST request to FastAPI (/predict)
        ↓
Model Pipeline (preprocessing + prediction)
        ↓
Prediction + Confidence returned
        ↓
Displayed in UI
```

---

## ⚙️ Setup & Run Locally

### 1. Clone the repository

```id="y6u2j8"
git clone https://github.com/YuvarajGML/weather-ml-app.git
cd weather-ml-app
```

---

### 2. Install dependencies

```id="n8q3vc"
pip install -r requirements.txt
```

---

### 3. Run FastAPI backend

```id="7m2f7v"
uvicorn backend.fastapi_app:app --reload
```

Backend runs at:

```id="u3f8md"
http://127.0.0.1:8000
```

---

### 4. Run Streamlit frontend

```id="2k9dwr"
streamlit run frontend/streamlit_app.py
```

Frontend runs at:

```id="x6b1re"
http://localhost:8501
```

---

## 🧪 Example Input

```json id="m8f2pk"
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

---

## 📊 Example Output

```json id="g5r9vx"
{
  "prediction": "Rainy",
  "confidence": 0.87
}
```

---

## 💡 Key Engineering Highlights

* Designed a **robust ML pipeline** to prevent feature mismatch errors
* Handled **categorical encoding within the pipeline**
* Ensured **consistent feature schema between training and inference**
* Built a **clean API interface for real-time predictions**
* Integrated frontend and backend seamlessly

---

## 🚀 Future Improvements

* Deploy backend (Render / Railway)
* Deploy frontend (Streamlit Cloud)
* Add batch prediction endpoint
* Add analytics dashboard

---

## 👨‍💻 Author

**Yuvaraj Gopi**
