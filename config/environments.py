import os
from dotenv import load_dotenv

load_dotenv()

symbols = os.getenv("SYMBOLS")


class Config:
    APP_NAME = os.getenv("APP_NAME", "X-Particle")
    APP_ENV = os.getenv("APP_ENV", "development")
    PORT = int(os.getenv("PORT", "3333"))
    APP_VERSION = os.getenv("APP_VERSION", "0.0.1")
    MAGIC_NUMBER = int(os.getenv("MAGIC_NUMBER", "99"))

    GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")
    if not GROQ_API_KEY:
        raise ValueError("GROQ_API_KEY not found in environment variables")

    TAVILY_API_KEY = os.getenv("TAVILY_API_KEY", "")
    if not TAVILY_API_KEY:
        raise ValueError("TAVILY_API_KEY not found in environment variables")

    TEMPERATURE = float(os.getenv("TEMPERATURE", "0"))

    LOGIN = os.getenv("LOGIN")
    PASSWD = os.getenv("PASSWD")
    SERVER = os.getenv("SERVER")

    OFF_DAYS = os.getenv("OFF_DAYS", "Saturday,Sunday").split(",")

    if not symbols:
        raise ValueError("Symbols not found")
    SYMBOLS = symbols.split(",")


config = Config()
