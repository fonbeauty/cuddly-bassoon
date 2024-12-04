import logging

import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from contextlib import asynccontextmanager

from app.database.engine import delete_tables, create_tables
from app.database.repository import UserRepository
from app.routers import login, status, tasks, pages

logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(_: FastAPI):
    logger.warning("On startup")
    await delete_tables()
    logger.warning('Base cleared')
    await create_tables()
    await UserRepository.add_default_users()
    logger.warning('Admin created')
    yield
    logger.warning("On shutdown")


app = FastAPI(lifespan=lifespan)
app.include_router(pages.router)
app.include_router(login.router)
app.include_router(status.router)
app.include_router(tasks.router)

app.mount('/static', StaticFiles(directory='static'), 'static')

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)
