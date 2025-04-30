from pydantic import BaseModel
from typing import Optional
from datetime import date

class SurveySchema(BaseModel):
    id: Optional[int]
    first_name: str
    last_name: str
    street_address: Optional[str]
    city: Optional[str]
    state: Optional[str]
    zip: Optional[str]
    phone: Optional[str]
    email: str
    survey_date: date
    liked_most: Optional[str]
    interested_via: Optional[str]
    recommendation: Optional[str]

    class Config:
        orm_mode = True
