from typing import Annotated

from fastapi import APIRouter, Depends

from app.database.repository import TaskRepository
from app.models.schemas import TaskAdd, TaskId, Task

router = APIRouter(prefix='/tasks', tags=['Задачи'])


@router.post('')
async def add_task(task: Annotated[TaskAdd, Depends()]) -> TaskId:
    task_id = await TaskRepository.add_one(task)
    return TaskId(result='Success', task_id=task_id)


@router.get('')
async def get_tasks() -> list[Task]:
    tasks = await TaskRepository.get_all()
    return tasks
