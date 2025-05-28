from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

MYSQL_USER = settings.MYSQL_USER
MYSQL_PASSWORD = settings.MYSQL_PASSWORD
DOCKER_DB_VOLNAME = settings.DOCKER_DB_VOLNAME
DB_PORT = settings.DB_PORT
MYSQL_DATABASE = settings.MYSQL_DATABASE

SQLALCHEMY_DATABASE_URL = f"mysql+mysqlconnector://{MYSQL_USER}:{MYSQL_PASSWORD}@{DOCKER_DB_VOLNAME}:{DB_PORT}/{MYSQL_DATABASE}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

