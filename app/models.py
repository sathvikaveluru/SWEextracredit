from sqlalchemy import Column, Integer, String, Date
from app.database import Base

class Survey(Base):
    __tablename__ = "surveys"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(255), nullable=False)
    last_name = Column(String(255), nullable=False)
    street_address = Column(String(255))
    city = Column(String(255))
    state = Column(String(255))
    zip = Column(String(20))
    phone = Column(String(20))
    email = Column(String(255), nullable=False)
    survey_date = Column(Date, nullable=False)
    liked_most = Column(String(255))
    interested_via = Column(String(255))
    recommendation = Column(String(50))
