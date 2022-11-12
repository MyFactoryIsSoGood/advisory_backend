from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import parse_obj_as
from typing import List

from schemas.users import Broker, BrokerBase, Rate, RateBase
from controllers.controllers import BrokerController, RateController

router = APIRouter(prefix="/rates", tags=["rates"])


@router.post("/", response_model=Rate, status_code=status.HTTP_201_CREATED)
def store_broker(rate: RateBase, rates: RateController = Depends()):
    db_rate = rates.create(rate)
    return Rate.from_orm(db_rate)
