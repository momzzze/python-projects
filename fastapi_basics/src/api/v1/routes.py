from fastapi import APIRouter
from src.api.v1.auth.routes import router as auth_router

router=APIRouter()

@router.get("/")
def read_root():
    return {"Hello": "World"}

router.include_router(auth_router)