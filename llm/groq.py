from langchain_groq import ChatGroq
from config.environments import config


llm = ChatGroq(
    api_key=config.GROQ_API_KEY,  # type: ignore
    temperature=config.TEMPERATURE,
    # model="openai/gpt-oss-120b",
    # model="llama-3.1-8b-instant",
    model="openai/gpt-oss-120b",
)
