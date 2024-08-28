from fastapi import APIRouter

from app.database.repository import UserRepository
from app.models.schemas import User, UserLogin

router = APIRouter(prefix='/login', tags=['Логин'])


# @login_router.get('')
# async def get_users() -> list[User]:
#     users = await UserRepository.get_all()
#     return users


@router.post('')
async def login(user: UserLogin):
    # Authenticate the user here (e.g., check against a database)
    if user:
        print(user)
        return {"message": "Login successful"}
    else:
        return {"message": "Invalid username or password"}


@router.post('/registration')
async def registration(username: str, password: str):
    # Authenticate the user here (e.g., check against a database)
    if authenticate(username, password):
        return {"message": "Login successful"}
    else:
        return {"message": "Invalid username or password"}


def authenticate(username: str, password: str) -> bool:
    # TO DO: implement actual authentication logic here
    return True  # Replace with actual authentication logic
