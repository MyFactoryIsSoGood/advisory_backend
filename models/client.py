

from sqlalchemy import Column, String, Float, Integer

from database import Model


class Client(Model):
    __tablename__ = "clients"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    #brokerID
    yearIncomePercent = Column(Float)
