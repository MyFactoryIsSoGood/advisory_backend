from fastapi import FastAPI
from pydantic import BaseModel

from database import Model, engine
from routes import rates
from routes import brokers
from routes import users
from routes import bot


Model.metadata.create_all(bind=engine)
app = FastAPI()
app.include_router(rates.router)
app.include_router(brokers.router)
app.include_router(users.router)
app.include_router(bot.router)

