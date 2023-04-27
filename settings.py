from pydantic import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "Project title"
    SQLALCHEMY_DATABASE_URI: str = "sqlite:///app.db"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
