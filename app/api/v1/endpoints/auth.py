from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from app.core.utils.deps import DB_DEPENDENCY

router = APIRouter()

@router.post("/login")
async def login(
    db: DB_DEPENDENCY,
    form_data: OAuth2PasswordRequestForm = Depends()
):
    """
    ユーザーログインエンドポイント
    """
    # TODO: 実際の認証ロジックを実装
    return {"message": "Login endpoint"}

@router.post("/register")
async def register(
    db: DB_DEPENDENCY
):
    """
    ユーザー登録エンドポイント
    """
    # TODO: 実際の登録ロジックを実装
    return {"message": "Register endpoint"}
