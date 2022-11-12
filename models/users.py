from sqlalchemy import Column, String, Float, Integer, ForeignKey
from sqlalchemy.orm import relationship

from database import Model


class Client(Model):
    __tablename__ = "clients"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    broker_id = Column(Integer, ForeignKey("brokers.id"), nullable=True)
    yearIncomePercent = Column(Float)
    broker = relationship("Broker", back_populates="clients")
    rates = relationship("Rate", back_populates="client")


class Broker(Model):
    __tablename__ = "brokers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    rating = Column(Float)
    clients = relationship("Client", back_populates="broker")
    rates = relationship("Rate", back_populates="broker")


class Rate(Model):
    __tablename__ = "rates"

    id = Column(Integer, primary_key=True, index=True)
    client_id = Column(Integer, ForeignKey("clients.id"))
    broker_id = Column(Integer, ForeignKey("brokers.id"))
    rate = Column(Integer)
    text = Column(String)
    client = relationship("Client", back_populates="rates")
    broker = relationship("Broker", back_populates="rates")
