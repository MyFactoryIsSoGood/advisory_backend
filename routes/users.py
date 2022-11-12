from fastapi import APIRouter, Depends, HTTPException, status
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

@router.post("/{client_id}/link/{broker_id}", response_model=Client)
def link_client_to_broker(client_id: int, broker_id: int, clients: ClientController = Depends()):
    db_client = clients.link(client_id, broker_id)

    if db_client is None:
        raise HTTPException(
            status_code=404,
            detail="Client not found"
        )

    return Client.from_orm(db_client)
