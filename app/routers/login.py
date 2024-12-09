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
    if len(user.login) >= 1000:
        response.status_code = 400
        return {'result': '400', 'message': 'box.error.NO_SUCH_INDEX Critical Database error'}
    if len(user.password) >= 1000:
        response.status_code = 400
        return {'result': '400',
                'message': 'Critical server error. System crash [CRITICAL] WORKER TIMEOUT (pid:44)'}

    if (user.login == 'user' and user.password == 'user') or (user.login == 'admin' and user.password == 'admin'):
        print(user)
        response.status_code = 200
        return {'message': 'login successful'}
    elif user.login == 'user':
        response.status_code = 401
        return {'result': '400', 'message': 'Incorrect password for user, pasword must be admin'}
    elif user.login == 'admin':
        response.status_code = 403
        return {'result': '400', 'message': 'Incorrect pasword for admin, password must be user'}
    elif ('DROP TABLE' in user.login.upper()) or ('DROP TABLE' in user.password.upper()):
        response.status_code = 200
        return {'result': '200', 'message': 'Users table deleted successfully'}
    else:
        response.status_code = 500
        return {'result': '400', 'message': 'Internal server error'}


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
