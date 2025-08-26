import time

from fastapi import APIRouter, Response

from app.common.logging_config import produce_logger
from app.database.repository import UserRepository
from app.models.schemas import User, UserLogin

logger = produce_logger(__name__)
router = APIRouter(prefix='/login', tags=['Логин'])


# @login_router.get('')
# async def get_users() -> list[User]:
#     users = await UserRepository.get_all()
#     return users


@router.post('', status_code=200)
async def login(user: UserLogin, response: Response) -> dict:
    # Authenticate the user here (e.g., check against a database)
    if ('user' in user.login and user.password == 'user') or ('admin' in user.login and user.password == 'admin'):
        print(user)
        logger.info(f'Requested user login. User {user.login} login successfully')
        return {'message': 'login successful'}
    else:
        response.status_code = 401
        # return {'result': '401', 'message': 'Invalid username or password'}
        msg = {'result': '401', 'message': 'Unauthorised'}
        logger.error(f'Requested user {user.login} login failed. Invalid username'
                     f' or password {response.status_code} {msg}')
        return msg


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
