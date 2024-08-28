from typing import Annotated

from fastapi import Depends, APIRouter

from repository import TaskRepository, UserRepository
from schemas import TaskAdd, Task, TaskId, User, UserLogin

common_router = APIRouter(
    prefix='',
    tags=['Инфо']
)

tasks_router = APIRouter(
    prefix='/api/tasks',
    tags=['Задачи']
)

login_router = APIRouter(
    prefix='/api/login',
    tags=['Логин']
)


@common_router.get('/info')
async def info():
    return {'Application name': 'Cuddly Bassoon'}


@tasks_router.post('')
async def add_task(task: Annotated[TaskAdd, Depends()]) -> TaskId:
    task_id = await TaskRepository.add_one(task)
    return TaskId(result='Success', task_id=task_id)


@tasks_router.get('')
async def get_tasks() -> list[Task]:
    tasks = await TaskRepository.get_all()
    return tasks


@login_router.get('')
async def get_users() -> list[User]:
    users = await UserRepository.get_all()
    return users


@login_router.post('')
async def login(user: UserLogin):
    # Authenticate the user here (e.g., check against a database)
    if user:
        print(user)
        return {"message": "Login successful"}
    else:
        return {"message": "Invalid username or password"}


@login_router.post('/registration')
async def registration(username: str, password: str):
    # Authenticate the user here (e.g., check against a database)
    if authenticate(username, password):
        return {"message": "Login successful"}
    else:
        return {"message": "Invalid username or password"}


def authenticate(username: str, password: str) -> bool:
    # TO DO: implement actual authentication logic here
    return True  # Replace with actual authentication logic
