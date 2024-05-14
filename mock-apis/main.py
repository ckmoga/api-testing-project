from fastapi import FastAPI
from .src.routers import users, books
import logging
app = FastAPI()

app.include_router(users.router)
app.include_router(books.router)

logging.info('Created FASTAPI instance')

@app.get("/")
def read_root():
    return {"Hello": "World"}