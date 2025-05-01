from fastapi import FastAPI, Form, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import Survey
from datetime import datetime
from app.schemas import SurveySchema
from typing import List
from fastapi import HTTPException
from dotenv import load_dotenv
load_dotenv(dotenv_path=".env")

app = FastAPI()

templates = Jinja2Templates(directory="templates")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/survey-form")
async def survey_form(request: Request):
    return templates.TemplateResponse("survey_form.html", {"request": request})

@app.get("/get-surveys", response_model=List[SurveySchema])
async def get_surveys(db: Session = Depends(get_db)):
    surveys = db.query(Survey).all()
    return surveys

@app.post("/submit-survey")
async def submit_survey(
    request: Request,
    first_name: str = Form(...),
    last_name: str = Form(...),
    street_address: str = Form(None),
    city: str = Form(None),
    state: str = Form(None),
    zip: str = Form(None),
    phone: str = Form(None),
    email: str = Form(...),
    survey_date: str = Form(...),
    liked_most: str = Form(None),
    interested_via: str = Form(None),
    recommendation: str = Form(None),
):
    db: Session = SessionLocal()

    survey_date_obj = datetime.strptime(survey_date, "%Y-%m-%d").date()

    survey = Survey(
        first_name=first_name,
        last_name=last_name,
        street_address=street_address,
        city=city,
        state=state,
        zip=zip,
        phone=phone,
        email=email,
        survey_date=survey_date_obj,
        liked_most=liked_most,
        interested_via=interested_via,
        recommendation=recommendation
    )

    db.add(survey)
    db.commit()
    db.close()

    return templates.TemplateResponse("success.html", {"request": request})

@app.delete("/delete-survey/{survey_id}")
async def delete_survey(survey_id: int, db: Session = Depends(get_db)):
    survey = db.query(Survey).filter(Survey.id == survey_id).first()
    if survey is None:
        raise HTTPException(status_code=404, detail="Survey not found")
    
    db.delete(survey)
    db.commit()
    return {"message": f"Survey {survey_id} deleted successfully"}

@app.put("/update-survey/{survey_id}")
async def update_survey(
    survey_id: int,
    first_name: str = Form(None),
    last_name: str = Form(None),
    street_address: str = Form(None),
    city: str = Form(None),
    state: str = Form(None),
    zip: str = Form(None),
    phone: str = Form(None),
    email: str = Form(None),
    survey_date: str = Form(None),
    liked_most: str = Form(None),
    interested_via: str = Form(None),
    recommendation: str = Form(None),
    db: Session = Depends(get_db)
):
    survey = db.query(Survey).filter(Survey.id == survey_id).first()
    if survey is None:
        raise HTTPException(status_code=404, detail="Survey not found")
    
    if first_name: survey.first_name = first_name
    if last_name: survey.last_name = last_name
    if street_address: survey.street_address = street_address
    if city: survey.city = city
    if state: survey.state = state
    if zip: survey.zip = zip
    if phone: survey.phone = phone
    if email: survey.email = email
    if survey_date: survey.survey_date = datetime.strptime(survey_date, "%Y-%m-%d").date()
    if liked_most: survey.liked_most = liked_most
    if interested_via: survey.interested_via = interested_via
    if recommendation: survey.recommendation = recommendation

    db.commit()
    return {"message": f"Survey {survey_id} updated successfully"}
