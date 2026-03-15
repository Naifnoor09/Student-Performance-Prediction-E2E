# 📚 Student Performance Prediction — End to End ML Project

A complete end-to-end machine learning project that predicts a student's **Performance Index** based on study habits and lifestyle factors. Built with a FastAPI backend, Streamlit frontend, and fully containerized with Docker.

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
- **Features:**

| Feature | Description |
|---|---|
| Hours Studied | Daily hours spent studying |
| Previous Scores | Scores from previous exams |
| Extracurricular Activities | Yes / No |
| Sleep Hours | Average hours of sleep per night |
| Sample Question Papers Practiced | Number of practice papers attempted |

- **Preprocessing:** `StandardScaler` for numerical features, `OneHotEncoder` for categorical
- **Pipeline:** `ColumnTransformer` → `LinearRegression`
- **Serialization:** `joblib`

---

## ⚙️ Backend — FastAPI

- `POST /predict` — Takes student details, returns predicted Performance Index
- `GET /health` — Check if model is loaded and API is running
- `GET /` — Welcome page

**Sample Input:**
```json
{
  "hours_studied": 7,
  "previous_scores": 85,
  "extracurricular_activities": "Yes",
  "sleep_hours": 7,
  "sample_question_papers_practiced": 5
}
```

**Sample Output:**
```json
{
  "predicted_performance_index": 54.11
}
```

---

## 🎨 Frontend — Streamlit

- Clean input form for all 5 features
- Instant Performance Index prediction
- Connects to FastAPI backend

---

## 🐳 Run with Docker

Both FastAPI and Streamlit are packaged in a single Docker container.

### 1. Build the image
```bash
docker build -t student-performance .
```

### 2. Run the container
```bash
docker run -p 8000:8000 -p 8501:8501 student-performance
```

### 3. Open in browser
- **Streamlit Dashboard** → `http://localhost:8501`
- **FastAPI Swagger Docs** → `http://localhost:8000/docs`

---

## 🚀 Run Without Docker

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Start FastAPI (Terminal 1)
```bash
cd src/backend
uvicorn main:app --reload
```

### 3. Start Streamlit (Terminal 2)
```bash
cd src/frontend
streamlit run app.py
```

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| ML | scikit-learn, Linear Regression |
| API | FastAPI, Pydantic |
| Dashboard | Streamlit |
| Data | Pandas, NumPy |
| Serialization | Joblib |
| Containerization | Docker |

---

## 👤 Author

**Mohammad Naif** — Cool Data Science Undergrad Student 
