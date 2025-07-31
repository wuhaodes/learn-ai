import os
import openai  # type: ignore
from dotenv import load_dotenv, find_dotenv
from openai import OpenAI  # type: ignore


def get_openai_key():
    _ = load_dotenv(find_dotenv())
    return os.getenv("OPENAI_API_KEY")


def get_completion(prompt, temperature=1):
    client = OpenAI(api_key=get_openai_key(), base_url="https://api.deepseek.com")
    messages = [
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": prompt},
    ]
    response = client.chat.completions.create(
        model="deepseek-chat", messages=messages, temperature=temperature
    )
    return response.choices[0].message.content
