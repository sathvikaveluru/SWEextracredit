from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from typing import List
from pydantic import BaseModel, EmailStr
from datetime import date

# Create FastAPI app instance
app = FastAPI()

# In-memory surveys list
surveys = []

# Set up templates folder
templates = Jinja2Templates(directory="templates")

# Your Survey Model (optional, if you want to use /surveys GET too)
class Survey(BaseModel):
    first_name: str
    last_name: str
    street_address: str = None
    city: str = None
    state: str = None
    zip: str = None
    phone: str = None
    email: EmailStr
    survey_date: date
    liked_most: str
    interested_via: str
    recommendation: str

# Serve Survey Form
@app.get("/survey-form", response_class=HTMLResponse)
def get_survey_form(request: Request):
    return templates.TemplateResponse("survey_form.html", {"request": request})

# Handle form submission
@app.post("/submit-survey")
async def submit_survey(
    first_name: str = Form(...),
    last_name: str = Form(...),
    street_address: str = Form(None),
    city: str = Form(None),
    state: str = Form(None),
    zip: str = Form(None),
    phone: str = Form(None),
    email: str = Form(...),
    survey_date: str = Form(...),
    liked_most: str = Form(...),
    interested_via: str = Form(...),
    recommendation: str = Form(...)
):
    survey = {
        "first_name": first_name,
        "last_name": last_name,
        "street_address": street_address,
        "city": city,
        "state": state,
        "zip": zip,
        "phone": phone,
        "email": email,
        "survey_date": survey_date,
        "liked_most": liked_most,
        "interested_via": interested_via,
        "recommendation": recommendation
    }
    surveys.append(survey)
    return RedirectResponse(url="/survey-form", status_code=303)

# (Optional) View submitted surveys
@app.get("/surveys", response_model=List[Survey])
def get_surveys():
    return surveys
