from typing import Annotated
from fastapi import Depends
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.repositories.user import UserRepository
from app.services.user import UserService

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Type alias for database session dependency injection
DB_DEPENDENCY = Annotated[Session, Depends(get_db)]

def get_user_repository(db: DB_DEPENDENCY) -> UserRepository:
    return UserRepository(db)

USER_REPOSITORY_DEPENDENCY = Annotated[UserRepository, Depends(get_user_repository)]

def get_user_service(user_repository: USER_REPOSITORY_DEPENDENCY) -> UserService:
    return UserService(user_repository)

USER_SERVICE_DEPENDENCY = Annotated[UserService, Depends(get_user_service)]