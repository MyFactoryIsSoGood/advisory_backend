from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import parse_obj_as
from typing import List

from schemas.users import Broker, BrokerBase
from controllers.controllers import BrokerController

router = APIRouter(prefix="/brokers", tags=["brokers"])


@router.get("/", response_model=List[Broker])
def list_brokers(skip: int = 0, max: int = 10, brokers: BrokerController = Depends()):
    db_brokers = brokers.all(skip=skip, max=max)
    return parse_obj_as(List[Broker], db_brokers)


@router.post("/", response_model=Broker, status_code=status.HTTP_201_CREATED)
def store_broker(broker: BrokerBase, brokers: BrokerController = Depends()):
    db_broker = brokers.create(broker)
    return Broker.from_orm(db_broker)


@router.get("/{broker_id}", response_model=Broker)
def get_broker(broker_id: int, brokers: BrokerController = Depends()):
    db_broker = brokers.find(broker_id)

    if db_broker is None:
        raise HTTPException(
            status_code=404,
            detail="Broker not found"
        )

    return Broker.from_orm(db_broker)
