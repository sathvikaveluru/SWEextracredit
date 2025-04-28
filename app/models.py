from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Survey(Base):
    __tablename__ = "surveys"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    street_address = Column(String(100), nullable=False)
    city = Column(String(50), nullable=False)
    state = Column(String(20), nullable=False)
    zip_code = Column(String(10), nullable=False)
    phone = Column(String(20), nullable=False)
    email = Column(String(100), nullable=False)
    survey_date = Column(Date, nullable=False)

    liked_most = Column(String(50), nullable=False)  # e.g., 'students'
    interested_via = Column(String(50), nullable=False)  # e.g., 'internet'
    recommendation = Column(String(20), nullable=False)  # e.g., 'Very Likely'
