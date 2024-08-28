import logging

import uvicorn
from fastapi import FastAPI

from contextlib import asynccontextmanager

from app.database.engine import delete_tables, create_tables
from app.database.repository import UserRepository
from app.routers import login, status, tasks


@asynccontextmanager
async def lifespan(_: FastAPI):
    logging.warning("On startup")
    await delete_tables()
    logging.warning('Base cleared')
    await create_tables()
    await UserRepository.add_default_users()
    logging.warning('Admin created')
    yield
    logging.warning("On shutdown")


app = FastAPI(lifespan=lifespan)
app.include_router(login.router)
app.include_router(status.router)
app.include_router(tasks.router)

if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)
