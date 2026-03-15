# 📚 Student Performance Prediction — End to End ML Product

## ❗ Problem Statement

Identifying at-risk students early can significantly improve academic outcomes — but schools often lack tools to flag struggling students before exams. This product predicts a student's Performance Index based on study habits and lifestyle inputs, enabling educators and students to take proactive action before it's too late.

---

## 📁 Project Structure

```
Student Performance Prediction E2E/
├── data/
│   └── student_performance.csv      ← Dataset
├── model/
│   └── model.pkl                    ← Trained pipeline (scaler + model)
├── notebook/
│   └── notebook.ipynb               ← EDA, training, evaluation
├── src/
│   ├── backend/
│   │   └── main.py                  ← FastAPI app
│   └── frontend/
│       └── app.py                   ← Streamlit dashboard
├── Dockerfile                       ← Runs both FastAPI + Streamlit
├── requirements.txt
└── README.md
```

---

## 🧠 ML Pipeline

- **Task:** Regression — predicts a continuous Performance Index
- **Preprocessing:** StandardScaler + OneHotEncoder via ColumnTransformer
- **Model:** Linear Regression Pipeline
- **Serialization:** joblib

**Input Features:**

| Feature | Description |
|---|---|
| Hours Studied | Daily hours spent studying |
| Previous Scores | Scores from previous exams |
| Extracurricular Activities | Yes / No |
| Sleep Hours | Average hours of sleep per night |
| Sample Question Papers Practiced | Number of practice papers attempted |

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| ML | scikit-learn, Linear Regression |
| API | FastAPI, Pydantic, Uvicorn |
| Dashboard | Streamlit |
| Data | Pandas, NumPy |
| Serialization | Joblib |
| Containerization | Docker |

---

## 🚀 How to Run

### Option A — Docker (Recommended)
```bash
# Build the image
docker build -t student-performance .

# Run the container
docker run -p 8000:8000 -p 8501:8501 student-performance
```

- **Streamlit Dashboard** → `http://localhost:8501`
- **FastAPI Swagger Docs** → `http://localhost:8000/docs`

### Option B — Without Docker

```bash
# Install dependencies
pip install -r requirements.txt

# Terminal 1 — FastAPI
cd src/backend
uvicorn main:app --reload

# Terminal 2 — Streamlit
cd src/frontend
streamlit run app.py
```

---

## 📊 Sample Prediction

**Input:**
```json
{
  "hours_studied": 7,
  "previous_scores": 85,
  "extracurricular_activities": "Yes",
  "sleep_hours": 7,
  "sample_question_papers_practiced": 5
}
```

**Output:**
```json
{
  "predicted_performance_index": 54.11
}
```

---

## 👤 Author

**Mohammad Naif** — Cool Data Science Undergrad Student  
