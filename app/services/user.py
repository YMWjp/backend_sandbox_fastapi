# app/services/user.py
from app.domain.models.user import User
from app.domain.schemas.user import UserCreate, UserInDB

class UserService:
    async def create_user(self, user_data: UserCreate) -> UserInDB:
        user = User(
            email=user_data.email,
            hashed_password=self._hash_password(user_data.password)
        )
        db_user = await self.user_repository.create_user(user)
        return UserInDB.model_validate(db_user)
    
    async def get_user_by_email(self, email: str) -> User | None:
        return await self.user_repository.get_user_by_email(email)
    
    async def get_user_by_id(self, user_id: int) -> User | None:
        return await self.user_repository.get_user_by_id(user_id)
    
    # async def update_user(self, user_id: int, user_data: UserUpdate) -> User | None:
    #     user = await self.get_user_by_id(user_id)
    #     if not user:
    #         return None
    #     user.update(user_data)
    #     return await self.user_repository.update_user(user)
    
    async def delete_user(self, user_id: int) -> None:
        user = await self.get_user_by_id(user_id)
        if not user:
            return None
        await self.user_repository.delete_user(user)