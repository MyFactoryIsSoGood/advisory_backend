from pydantic import BaseModel


class BrokerBase(BaseModel):
    name: str


class Broker(BrokerBase):
    id: int
    rating: float

    class Config:
        orm_mode = True
