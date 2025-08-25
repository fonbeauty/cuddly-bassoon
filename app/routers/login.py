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
    if len(user.login) >= 1000:
        response.status_code = 400
        msg = {'result': '400', 'message': 'box.error.NO_SUCH_INDEX Critical Database error'}
        logger.error(f'Requested user {user.login} login failed. Login too long. Database error.'
                     f'\n {response.status_code} {msg}')
        return msg
    if len(user.password) >= 1000:
        response.status_code = 400
        msg = {'result': '400',
               'message': 'Critical server error. System crash [CRITICAL] WORKER TIMEOUT (pid:44)'}
        logger.error(f'Requested user {user.login} login failed. Password too long: {user.password}.'
                     f' Server critical error. \n {response.status_code} {msg}')
        return msg

    if (user.login == 'user' and user.password == 'user') or (user.login == 'admin' and user.password == 'admin'):
        print(user)
        response.status_code = 200
        logger.info(f'Requested user login. User {user.login} login successfully')
        return {'message': 'login successful'}
    elif (user.login == 'user') or (user.login == 'admin'):
        response.status_code = 401
        msg = {'result': '401', 'message': 'Unauthorthorized'}
        logger.error(f'Requested user {user.login} login failed. Incorrect pasword {response.status_code} {msg}')
        return msg
    elif ('DROP TABLE' in user.login.upper()) or ('DROP TABLE' in user.password.upper()):
        response.status_code = 200
        logger.info(f'Requested user login. User {user.login} login successfully')
        logger.info(f'Executing SQL command "DROP TABLE User"')
        logger.info(f'SQL command "DROP TABLE User" completed successfully. Table User deleted.')
        return {'result': '200', 'message': 'table Users deleted successfully'}
    else:
        response.status_code = 400
        msg = {'result': '400', 'message': 'Internal server error'}
        logger.error(f'Requested user {user.login} login failed. Unknown error {msg}')
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
