from fastapi import APIRouter, Response

from app.database.repository import UserRepository
from app.models.schemas import User, UserLogin

router = APIRouter(prefix='/login', tags=['Логин'])


# @login_router.get('')
# async def get_users() -> list[User]:
#     users = await UserRepository.get_all()
#     return users


@router.post('', status_code=200)
async def login(user: UserLogin, response: Response) -> dict:
    # Authenticate the user here (e.g., check against a database)
    if (user.login == 'user' and user.password == 'user') or (user.login == 'admin' and user.password == 'admin'):
        print(user)
        return {'message': 'login successful'}
    else:
        response.status_code = 401
        return {'result': '401', 'message': 'Invalid username or password'}


@router.post('/registration')
async def registration(username: str, password: str):
    # Authenticate the user here (e.g., check against a database)
    if authenticate(username, password):
        return {'message': 'Login successful'}
    else:
        return {'message': 'Invalid username or password'}


def authenticate(username: str, password: str) -> bool:
    # TO DO: implement actual authentication logic here
    return True  # Replace with actual authentication logic
