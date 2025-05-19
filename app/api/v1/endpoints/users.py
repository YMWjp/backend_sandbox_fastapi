from fastapi import APIRouter
from app.db.session import DB_DEPENDENCY

router = APIRouter()

@router.get("/me")
async def read_users_me(
    db: DB_DEPENDENCY = None
):
    """
    現在のユーザー情報を取得
    """
    # TODO: 実際のユーザー情報取得ロジックを実装
    return {"message": "Get current user"}

@router.get("/{user_id}")
async def read_user(
    user_id: int,
    db: DB_DEPENDENCY = None
):
    """
    指定されたIDのユーザー情報を取得
    """
    # TODO: 実際のユーザー情報取得ロジックを実装
    return {"message": f"Get user {user_id}"}
