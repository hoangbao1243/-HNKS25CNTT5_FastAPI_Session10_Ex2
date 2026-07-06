from fastapi import FastAPI

from database import Base, engine
from routers.customers import router

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router)