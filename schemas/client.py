from pydantic import BaseModel


class ClientBase(BaseModel):
    name: str
    yearIncomePercent: float


class Client(ClientBase):
    id: int

    class Config:
        orm_mode = True
