from sqlalchemy.orm import Session
from app.domain.models.user import User

class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    async def create_user(self, user: User) -> User:
        self.db.add(user)
        await self.db.commit()
        await self.db.refresh(user)
        return user
    
    async def get_user_by_email(self, email: str) -> User | None:
        return self.db.query(User).filter(User.email == email).first()

    async def get_user_by_id(self, user_id: int) -> User | None:
        return self.db.query(User).filter(User.id == user_id).first()
    
    async def update_user(self, user: User) -> User:
        self.db.add(user)
        await self.db.commit()
        await self.db.refresh(user)
        return user
    
    async def delete_user(self, user: User) -> None:
        await self.db.delete(user)
        await self.db.commit() 