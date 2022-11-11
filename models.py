from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    brokerID = Column(Integer, ForeignKey("brokers.id"), default=None)
    yearIncomePercent = Column(Integer)
    broker = relationship("Broker", back_populates="clients")

class Broker(Base):
    __tablename__ = "brokers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    clients = relationship("User", back_populates="broker")
    rating = Column(Integer)


