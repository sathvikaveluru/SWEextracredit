from pydantic import BaseModel, EmailStr, Field
from datetime import date

class SurveyBase(BaseModel):
    first_name: str
    last_name: str
    street_address: str
    city: str
    state: str
    zip_code: str
    phone: str
    email: EmailStr
    survey_date: date
    liked_most: str
    interested_via: str
    recommendation: str

class SurveyCreate(SurveyBase):
    pass

class SurveyUpdate(SurveyBase):
    pass

class SurveyResponse(SurveyBase):
    id: int

    class Config:
        orm_mode = True
