from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter(prefix='/pages', tags=['Фронтенд'])
templates = Jinja2Templates(directory='app/templates')


@router.get('/login')
async def login_html(request: Request):
    return templates.TemplateResponse(name='login.html', context={'request': request})


@router.get('/register')
async def register_html(request: Request):
    return templates.TemplateResponse(name='register.html', context={'request': request})


@router.get('/terms_and_conditions')
async def register_html(request: Request):
    return templates.TemplateResponse(name='terms_and_conditions.html', context={'request': request})


@router.get('/admin')
async def register_html(request: Request):
    return templates.TemplateResponse(name='admin.html', context={'request': request})


@router.get('/to_do_list')
async def register_html(request: Request):
    return templates.TemplateResponse(name='to_do_list.html', context={'request': request})
