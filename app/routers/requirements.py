from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter(tags=['Требования'])
templates = Jinja2Templates(directory='app/templates')


@router.get('/requirements')
async def requirements_html(request: Request):
    return templates.TemplateResponse(name='requirements.html', context={'request': request})
