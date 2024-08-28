from fastapi import APIRouter

router = APIRouter(tags=['Статус'])


@router.get('/status', status_code=200)
async def info():
    return {'Application name': 'Cuddly Bassoon'}
