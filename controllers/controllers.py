from typing import List

from fastapi.params import Depends
from sqlalchemy.orm import Session

from models.users import Client, Broker, Rate
from dependencies import get_db
from schemas.users import ClientBase, BrokerBase, RateBase


class ClientController:
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
            name=client.name
        )
        self.db.add(db_client)
        self.db.commit()
        self.db.refresh(db_client)

        return db_client

    def link(self, client_id: int, broker_id: int) -> Client:
        db_client = self.find(client_id)
        db_client.broker_id = broker_id
        self.db.commit()
        self.db.refresh(db_client)

        return db_client


class BrokerController:
    def __init__(self, db: Session = Depends(get_db)):
        self.db = db

    def find(self, id: int) -> Broker:
        query = self.db.query(Broker)
        return query.filter(Broker.id == id).first()

    def all(self, skip: int = 0, max: int = 100) -> List[Broker]:
        query = self.db.query(Broker)
        return query.offset(skip).limit(max).all()

    def create(self, broker: BrokerBase) -> Broker:
        db_broker = Broker(
            name=broker.name,
            level_risk=broker.level_risk
        )
        self.db.add(db_broker)
        self.db.commit()
        self.db.refresh(db_broker)

        return db_broker

    def change_rate(self, broker_id: int):
        db_broker = self.find(broker_id)
        db_broker.rating = sum([rate.rate for rate in db_broker.rates]) / len(db_broker.rates)
        self.db.commit()
        self.db.refresh(db_broker)

    def change_level_risk(self, broker_id: int, level_risk: int):
        db_broker = self.find(broker_id)
        db_broker.level_risk = level_risk
        self.db.commit()
        self.db.refresh(db_broker)


class RateController:
    def __init__(self, db: Session = Depends(get_db)):
        self.db = db

    def find(self, id: int) -> Rate:
        query = self.db.query(Rate)
        return query.filter(Rate.id == id).first()

    def all(self, skip: int = 0, max: int = 100) -> List[Rate]:
        query = self.db.query(Rate)
        return query.offset(skip).limit(max).all()

    def create(self, rate: RateBase) -> Rate:
        db_rate = Rate(
            rate=rate.rate,
            client_id=rate.client_id,
            broker_id=rate.broker_id,
            text=rate.text
        )
        self.db.add(db_rate)
        self.db.commit()
        self.db.refresh(db_rate)

        return db_rate
