from fastapi import APIRouter
from app.core.config import settings
from app.db.session import get_db
from sqlalchemy import text
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter()

@router.get("/health")
async def health_check():
    """
    Health check endpoint
    """ 
    return {"status": "ok"}

@router.get("/version")
async def get_version():
    """
    Return API version information
    """
    return {
        "version": settings.API_V1_STR,
    }

@router.get("/status")
async def get_status(db: AsyncSession = Depends(get_db)):
    """
    Return detailed status information of the system
    """
    try:
        # Database connection test
        await db.execute(text("SELECT 1"))
        db_status = "connected"
    except Exception as e:
        db_status = f"error: {str(e)}"

    return {
        "status": "operational",
        "version": settings.API_V1_STR,
        "database": db_status
    } 