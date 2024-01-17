from fastapi import APIRouter, Header, Body
from app.service.conta_service Import ContaService

router = APIRouter()

@router.get("/")
def get_conta(
        user: UserEmail,
        authorization: str = Header(...)):
    result = ContaService(authorization, user).get_user()
    return result

@router.post("/")
def post_conta(
    user: User,
    authorization: str = Header(...)):
    result = ContaService(authorization, user).get_user()
    return result

