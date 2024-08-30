from typing import Optional

from pydantic import BaseModel, ConfigDict


class TaskAdd(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    name: str
    description: Optional[str] = None


class Task(TaskAdd):
    id: int


class TaskId(BaseModel):
    result: str = 'Success'
    task_id: int


class UserAdd(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    username: str
    email: str
    password: str
    role: Optional[str] = 'user'


class User(UserAdd):
    id: int


class UserId(BaseModel):
    result: str = 'Success'
    user_id: int

class UserLogin(BaseModel):
    login: str
    password: str