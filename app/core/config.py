from pydantic_settings import BaseSettings
from pydantic import field_validator
import json

class Settings(BaseSettings):
    # Project
    ENV: str = "development"
    PROJECT_NAME: str = "FastAPI Backend"
    VERSION: str = "1.0.0"
    API_V1_STR: str = "/api/v1"
    
    # Database
    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_PORT: str = "3306"
    DB_NAME: str

    # MySQL
    MYSQL_ROOT_PASSWORD: str
    MYSQL_DATABASE: str
    MYSQL_USER: str
    MYSQL_PASSWORD: str
    MYSQL_PORT: str
    MYSQL_HOST: str

    # Docker
    DOCKER_DB_VOLNAME: str

    # CORS
    CORS_ORIGINS: list[str] = ["http://localhost:3000"]
    CORS_ALLOW_CREDENTIALS: bool = True
    CORS_ALLOW_METHODS: list[str] = ["GET", "POST", "PUT", "DELETE"]
    CORS_ALLOW_HEADERS: list[str] = ["Content-Type", "Authorization"]
    
    # JWT
    SECRET_KEY: str = ""
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    @field_validator("CORS_ORIGINS", "CORS_ALLOW_METHODS", "CORS_ALLOW_HEADERS", mode='before')
    def parse_list(cls, v):
        if isinstance(v, str):
            try:
                # expect string like '"["foo","bar"]"'
                return json.loads(v)
            except json.JSONDecodeError:
                # expect string like 'foo,bar'
                if v: # check if not empty string
                    return [item.strip() for item in v.split(",") if item.strip()]
                return [] # return empty list if empty string
        return v # return value if not string

    # Pydantic V2 style model config
    model_config = {
        "env_file": ".env",
        "env_file_encoding": "utf-8",
        "case_sensitive": True,
        "extra": "ignore"  # ignore items not defined in .env file
    }

settings = Settings()
