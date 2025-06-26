from pydantic_settings import BaseSettings
from pydantic import Field

class AppConfig(BaseSettings):
    APP_NAME: str = Field("EchoFlow", env="APP_NAME")
    DEBUG: bool = Field(False, env="DEBUG")
    DATABASE_URL: str = Field(..., env="DATABASE_URL")
    SECRET_KEY: str = Field(..., env="SECRET_KEY")
    JWT_ALGORITHM: str = Field("HS256", env="JWT_ALGORITHM")
    # Add more shared/global config here

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"