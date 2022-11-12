from fastapi import FastAPI

from database import Model, engine
from routes import routes


Model.metadata.create_all(bind=engine)
app = FastAPI()
app.include_router(routes.router)