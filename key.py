import os
import openai # type: ignore
from dotenv import load_dotenv, find_dotenv


def get_openai_key():
    _ = load_dotenv(find_dotenv())
    return os.getenv("OPENAI_API_KEY")

openai.api_key = get_openai_key()

print(openai.api_key)