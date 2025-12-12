from config.environments import config


def main():
    print(f"App Name: {config.APP_NAME}")
    print(f"App Version: {config.APP_VERSION}")
    print(f"App Environment: {config.APP_ENV}")
    print(f"Running on Port: {config.PORT}")
    print(f"Tavily API Key: {config.TAVILY_API_KEY}")
    print(f"OpenAI API Key: {config.OPENAI_API_KEY}")
    print(f"OpenAI API Temperature: {config.OPENAI_API_TEMPERATURE}")


if __name__ == "__main__":
    main()
