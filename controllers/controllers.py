from typing import List

from fastapi.params import Depends
from sqlalchemy.orm import Session

from models.client import Client
from models.broker import Broker
from dependencies import get_db
from schemas.client import ClientBase
from schemas.broker import BrokerBase


class Controller:
    def __init__(self, db: Session = Depends(get_db)):
        self.db = db

    def find(self, id: int) -> Client:
        query = self.db.query(Client)
        return query.filter(Client.id == id).first()

    def all(self, skip: int = 0, max: int = 100) -> List[Client]:
        query = self.db.query(Client)
        return query.offset(skip).limit(max).all()

    def create(self, client: ClientBase) -> Client:
        db_client = Client(
            name=client.name,
            yearIncomePercent=client.yearIncomePercent
        )
        self.db.add(db_client)
        self.db.commit()
        self.db.refresh(db_client)

        return db_client
