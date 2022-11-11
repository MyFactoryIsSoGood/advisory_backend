from sqlalchemy.orm import Session

import models
import schemas


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_broker(db: Session, user: schemas.BrokerCreate):
    db_user = models.Broker(name=user.name)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(name=user.name, brokerID=0, yearIncomePercent=0)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_brokers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Broker).offset(skip).limit(limit).all()


def create_broker_clients(db: Session, item: schemas.UserCreate, user_id: int):
    db_item = models.Broker(**item.dict(), brokerID=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
