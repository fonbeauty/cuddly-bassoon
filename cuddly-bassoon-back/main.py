import uvicorn
from fastapi import FastAPI

from contextlib import asynccontextmanager

from database import create_tables, delete_tables
from repository import UserRepository
from router import tasks_router, login_router, common_router
from schemas import UserAdd, UserId


@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print('База очищена')
    await create_tables()
    await UserRepository.add_default_users()
    print('admin created')
    yield
    print('Выклюечение')


app = FastAPI(lifespan=lifespan)
app.include_router(common_router)
app.include_router(tasks_router)
app.include_router(login_router)

if __name__ == '__main__':
    uvicorn.run(app, port=8003)
