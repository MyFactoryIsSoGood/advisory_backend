from fastapi import APIRouter, Depends, HTTPException, status, Request
from pydantic import parse_obj_as
from typing import List
from bs4 import BeautifulSoup
import requests

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


@router.post("/create_card")
async def create_card(req: Request):
    url = await req.json()
    page = requests.get(url['url'])
    page.encoding = 'utf8'

    soup = BeautifulSoup(page.text, "html.parser")

    title = soup.findAll('h1',
                         class_='Headlines_h2__M06yz Headlines_h--color-black__s26fH Headlines_h--font-secondary__6olW9 Headlines_h--mode-relative__9aaWD Headlines_h--color-black__s26fH ProductTop_headlines__mG4g_')
    info = soup.findAll('div',
                        class_='Text_p1__frpkE Text_p--mode-relative__p_124 Text_p--color-black__yElui Text_p--font-variant-inter-medium___QFLc HeadBar_headBarValue__l5srH')
    avatar = soup.findAll('div', class_='InstrumentIcon_instrumentIcon__uOA9D')
    style = avatar[0].get('style')

    return {
        "title": title[0].text,
        "abbreviated": info[0].text,
        "price": info[1].text,
        "forecast": info[2].text,
        "avatar": style[style.find("(") + 1:style.find(")")],
        "url": url["url"]
    }
