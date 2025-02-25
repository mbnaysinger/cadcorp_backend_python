from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "Bookstore API"
    APP_VERSION: str = "1.0.0"
    API_V1_STR: str = "/api/v1"
    DATABASE_URL: str = "postgresql://cad_user:cad123@db:5432/cadcorp_db"

    @property
    def DATABASE_URL_SQLALCHEMY(self):
        return self.DATABASE_URL.replace("postgres://", "postgresql://", 1)

    class Config:
        env_file = ".env"

settings = Settings()