from fastapi import FastAPI

from database import Model, engine
from routes import users, brokers, rates

Model.metadata.create_all(bind=engine)
app = FastAPI()
app.include_router(users.router)
app.include_router(brokers.router)
app.include_router(rates.router)