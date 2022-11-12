

from sqlalchemy import Column, String, Float, Integer

from database import Model


class Broker(Model):
    __tablename__ = "brokers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    rating = Column(Float)
