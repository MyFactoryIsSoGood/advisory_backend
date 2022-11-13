import collections

from fastapi import APIRouter, Depends, HTTPException, status, Request, Response
from starlette.status import HTTP_201_CREATED
from pydantic import parse_obj_as
from typing import List

from schemas.users import Client, ClientBase
from controllers.controllers import ClientController

router = APIRouter(prefix="/clients", tags=["clients"])


@router.get("/", response_model=List[Client])
def list_clients(skip: int = 0, max: int = 10, clients: ClientController = Depends()):
    db_clients = clients.all(skip=skip, max=max)
    return parse_obj_as(List[Client], db_clients)


@router.post("/", response_model=Client, status_code=status.HTTP_201_CREATED)
def store_clients(client: ClientBase, clients: ClientController = Depends()):
    db_client = clients.create(client)
    return Client.from_orm(db_client)


@router.get("/{client_id}", response_model=Client)
def get_clients(client_id: int, clients: ClientController = Depends()):
    db_client = clients.find(client_id)

    if db_client is None:
        raise HTTPException(
            status_code=404,
            detail="Client not found"
        )

    return Client.from_orm(db_client)


@router.post("/{client_id}/answer")
async def answer_client(req: Request, client_id: int, clients: ClientController = Depends()):
    types = {
        1: "Консеравтивный",
        2: "Сбалансированный",
        3: "Агрессивный"
    }
    body = await req.json()
    counts = collections.Counter([int(answer) for answer in body['answers']])
    if counts[4] > 4:
        inv_type = 3
    elif counts[3] > 4:
        inv_type = 2
    elif counts[2] > 4:
        inv_type = 1
    else:
        inv_type = 1

    db_client = clients.insert_type(client_id, inv_type)
    if db_client is None:
        raise HTTPException(
            status_code=404,
            detail="Client not found"
        )

    return {'invest_type': types[inv_type]}


@router.post("/{client_id}/link/{broker_id}", response_model=Client)
def link_client_to_broker(client_id: int, broker_id: int, clients: ClientController = Depends()):
    db_client = clients.link(client_id, broker_id)

    if db_client is None:
        raise HTTPException(
            status_code=404,
            detail="Client not found"
        )

    return Client.from_orm(db_client)
