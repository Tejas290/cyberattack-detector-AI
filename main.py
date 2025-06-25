from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import numpy as np
import joblib
import os

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

# Load model, scaler, and feature list
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model = joblib.load(os.path.join(BASE_DIR, "model.pkl"))
scaler = joblib.load(os.path.join(BASE_DIR, "scaler.pkl"))
features = joblib.load(os.path.join(BASE_DIR, "features.pkl"))

# ✅ Optional: load one row from dataset for default inputs (you can update this)
default_input_data = [0.0] * len(features)
default_input_data[0] = 60005445.0  # Example value for 'Flow Duration'
default_input_data[1] = 1.0         # Example value for 'Tot Fwd Pkts'
# You can add more if needed...

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {
        "request": request,
        "features": features,
        "input_data": default_input_data,
        "result": None
    })

@app.post("/predict", response_class=HTMLResponse)
async def predict(request: Request):
    form = await request.form()
    try:
        input_data = [float(form.get(f, 0.0)) for f in features]
        scaled_input = scaler.transform([input_data])
        prediction = model.predict(scaled_input)[0]
        label = "Benign" if prediction == 0 else "Attack"
    except Exception as e:
        label = f"Prediction Error: {str(e)}"
        input_data = default_input_data

    return templates.TemplateResponse("index.html", {
        "request": request,
        "features": features,
        "input_data": input_data,
        "result": label
    })
