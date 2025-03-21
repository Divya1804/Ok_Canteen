from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict

load_dotenv()

class Settings_Config(BaseSettings):
    DATABASE_URL: str
    JWT_SECRET_KEY: str
    JWT_ALGORITHM: str
    ACCESS_TOKEN_EXPIRY: int

    model_config = SettingsConfigDict(
        env_file="../../.env",
        extra="ignore"
    )

Config = Settings_Config()