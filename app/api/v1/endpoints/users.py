from fastapi import APIRouter
from app.core.utils.deps import USER_SERVICE_DEPENDENCY
from app.domain.schemas.user import UserInDB, UserCreate

router = APIRouter()

@router.post("/", response_model=UserInDB)
async def create_user(
    user_data: UserCreate,
    user_service: USER_SERVICE_DEPENDENCY
):
    user = await user_service.create_user(user_data)
    return user

@router.get("/")
async def read_users(
    user_service: USER_SERVICE_DEPENDENCY
):
    users = await user_service.get_users()
    return users

@router.get("/me")
async def read_users_me(
    user_service: USER_SERVICE_DEPENDENCY
):
    """
    現在のユーザー情報を取得
    """
    # TODO: 実際のユーザー情報取得ロジックを実装
    return {"message": "Get current user"}

@router.get("/{user_id}")
async def read_user(
    user_id: int,
    user_service: USER_SERVICE_DEPENDENCY
):
    """
    指定されたIDのユーザー情報を取得
    """
    # TODO: 実際のユーザー情報取得ロジックを実装
    return {"message": f"Get user {user_id}"}
