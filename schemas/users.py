from typing import Optional

from pydantic import BaseModel


class ClientBase(BaseModel):
    name: str


class Client(ClientBase):
    id: int
    yearIncomePercent: Optional[float] = None
    broker_id: Optional[int] = None

    class Config:
        orm_mode = True


class BrokerBase(BaseModel):
    name: str
    level_risk: Optional[int] = None


class Broker(BrokerBase):
    id: int
    rating: Optional[float] = None

    class Config:
        orm_mode = True


class RateBase(BaseModel):
    client_id: int
    broker_id: int
    rate: int
    text: Optional[str] = None


class Rate(RateBase):
    id: int

    class Config:
        orm_mode = True
