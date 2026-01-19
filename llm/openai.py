from langchain_openai import ChatOpenAI
from config.environments import config

model = ChatOpenAI(
    model="gpt-4o", temperature=config.TEMPERATURE, api_key=config.OPENAI_API_KEY  # type: ignore
)
