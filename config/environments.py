import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    APP_ENV = os.getenv("APP_ENV", "development")
    PORT = int(os.getenv("PORT", 3333))
    APP_NAME = os.getenv("APP_NAME", "X-Particle")
    APP_VERSION = os.getenv("APP_VERSION", "0.0.1")

    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
    GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")

    TEMPERATURE = float(os.getenv("TEMPERATURE", 0))

    TAVILY_API_KEY = os.getenv("TAVILY_API_KEY", "")

    LOGIN = os.getenv("LOGIN")
    PASSWD = os.getenv("PASSWD")
    SERVER = os.getenv("SERVER")


config = Config()
