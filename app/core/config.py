from pydantic_settings import BaseSettings

class Config(BaseSettings):
    api_host: str = "localhost:8000"
    db_host: str
    db_type: str
    postgres_user: str
    postgres_password: str
    postgres_port: str
    postgres_name: str
    debug: bool = False

    class Config:
        env_file = ".env"
        extra = "ignore"

config = Config()