from typing import Annotated
from fastapi import Depends
from sqlalchemy.orm import Session
from app.db.session import SessionLocal

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Type alias for database session dependency injection
DB_DEPENDENCY = Annotated[Session, Depends(get_db)]