from sqlalchemy import select

from database import new_session, TasksORM, UsersORM
from schemas import TaskAdd, Task, UserAdd, User


class TaskRepository:
    @classmethod
    async def add_one(cls, data: TaskAdd) -> int:
        async with new_session() as session:
            task_dict = data.model_dump()

            task = TasksORM(**task_dict)
            session.add(task)
            await session.flush()
            await session.commit()
            return task.id

    @classmethod
    async def get_all(cls) -> list[Task]:
        async with new_session() as session:
            query = select(TasksORM)
            result = await session.execute(query)
            task_models = result.scalars().all()
            task_schemas = [Task.model_validate(task_model) for task_model in task_models]
            return task_schemas


class UserRepository:
    @classmethod
    async def add_one(cls, data: UserAdd) -> int:
        async with new_session() as session:
            user_dict = data.model_dump()

            user = UsersORM(**user_dict)
            session.add(user)
            await session.flush()
            await session.commit()
            return user.id

    @classmethod
    async def get_all(cls) -> list[User]:
        async with new_session() as session:
            query = select(UsersORM)
            result = await session.execute(query)
            user_models = result.scalars().all()
            for user_model in user_models:
                print('Metadata', user_model.metadata)
                print('ID', user_model.id)
                print('email', user_model.email)
                print('username', user_model.username)
                print('password', user_model.password)
                print('role', user_model.role)
            user_schemas = [User.model_validate(user_model) for user_model in user_models]
            return user_schemas

    @classmethod
    async def add_default_users(self):
        async with new_session() as session:
            user = UserAdd(username='user', email='user@mail.ru', password='user')
            admin = UserAdd(username='admin', email='admin@mail.ru', password='admin', role='admin')
            user = UsersORM(**user.model_dump())
            admin = UsersORM(**admin.model_dump())
            session.add(user)
            session.add(admin)
            await session.commit()
