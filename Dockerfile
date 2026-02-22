FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000
EXPOSE 8501

# starting both backend + frontend
CMD sh -c "uvicorn src.backend.main:app --host 0.0.0.0 --port 8000 & streamlit run src/frontend/app.py --server.port=8501 --server.address=0.0.0.0"
