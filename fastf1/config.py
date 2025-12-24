import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    APP_NAME: str = "FastAPI Starter"
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./test.db")

settings = Settings()
