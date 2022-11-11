from typing import List, Union

from pydantic import BaseModel


class UserBase(BaseModel):
    name: str


class UserCreate(UserBase):
    pass


class User(UserBase):
    id: int
    brokerID: int
    yearIncomePercent: int

    class Config:
        orm_mode = True


class BrokerBase(BaseModel):
    name: str


class BrokerCreate(BrokerBase):
    pass


class Broker(BrokerBase):
    id: int
    rating: Union[str, None] = None
    clients: List[User] = []

    class Config:
        orm_mode = True
