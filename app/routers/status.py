from fastapi import APIRouter

from app.common.logging_config import produce_logger

logger = produce_logger(__name__)
router = APIRouter(tags=['Статус'])


@router.get('/status', status_code=200)
async def info():
    body = {
        'message_for_user': 'Glad to see you :)',
        'application_name': 'Cuddly Bassoon',
        'version': 'rare_1.2'
    }
    logger.info(f'Status endpoint accessed. Body: {body}')
    return body
