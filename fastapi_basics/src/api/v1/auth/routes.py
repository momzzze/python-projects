from fastapi import APIRouter
from .controller import login, register

router=APIRouter(prefix='/auth', tags=['Auth'])

@router.post('/login')
async def login_route():
    login()
    return{"message": "Login successful"}    

@router.post('/register')
async def register_route():
    register()
    return{"message": "Registration successful"}