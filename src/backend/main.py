import joblib
import pandas as pd
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Annotated, Literal
from enum import Enum
import os

app = FastAPI(title="Student Performance Prediction API", description="API to predict student performance based on various factors", version="1.0")

# Model Loading
MODEL_PATH = "model/model.joblib"

if not os.path.exists(MODEL_PATH):
    raise RuntimeError(f"Model file not found at {MODEL_PATH}")

try:
    model = joblib.load(MODEL_PATH)
except Exception as e:
    raise RuntimeError(f"Failed to load model {e}")


# Enums
class YesNo(str, Enum):
    Yes = "Yes"
    No = "No"
    
     
# Input Schema
class student_details(BaseModel):
    Hours_Studied : Annotated[float, Field(gt=0, le=24, description = "Hours studied per day")]
    Previous_Scores : Annotated[float, Field(ge=0, le=100, description="Previous exam score")]
    Extracurricular_Activities : YesNo
    Sleep_Hours : Annotated[float, Field(ge=0,le=24, description="Sleep hours per day")]
    Sample_Question_Papers_Practiced : Annotated[int, Field(ge=0, le=50, description="Number of sample question papers practiced")]
    

# Health Check
@app.get("/health")
def health():
    return {"status" : "ok", "model_loaded" : True}

# Prediction 
@app.post("/predict")
async def predict(data:student_details):
    try:
        df = pd.DataFrame([{
            "Hours Studied" : data.Hours_Studied,
            "Previous Scores": data.Previous_Scores,
            "Extracurricular Activities": data.Extracurricular_Activities.value,
            "Sleep Hours": data.Sleep_Hours,
            "Sample Question Papers Practiced": data.Sample_Question_Papers_Practiced
        }])
    
        prediction = model.predict(df)[0]
        return {
            "Performance Index" : round(float(prediction),2)
        }
        
    except Exception as e:
        raise HTTPException(
            status_code = 500,
            detail = f"Prediction Failed: {str(e)}"
        )

