import os
import openai  # type: ignore
from dotenv import load_dotenv, find_dotenv
from openai import OpenAI  # type: ignore


def get_openai_key():
    _ = load_dotenv(find_dotenv())
    return os.getenv("OPENAI_API_KEY")


def get_completion(prompt, model="deepseek-chat"):
    client = OpenAI(api_key=get_openai_key(), base_url="https://api.deepseek.com")
    messages = [{"role": "user", "content": prompt}]
    response = client.chat.completions.create(messages=messages, model=model)
    return response.choices[0].message.content
