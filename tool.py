import os
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


def get_completion_from_messages(
    messages, model="deepseek-chat", temperature=0, max_tokens=4096, stream=False
):
    client = OpenAI(api_key=get_openai_key(), base_url="https://api.deepseek.com")
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature,
        max_tokens=max_tokens,
        stream=stream,
    )
    return response.choices[0].message.content


def get_completion_and_token_count(
    messages, model="deepseek-chat", temperature=0, max_tokens=4096, stream=False
):
    client = OpenAI(api_key=get_openai_key(), base_url="https://api.deepseek.com")
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature,
        max_tokens=max_tokens,
        stream=stream,
    )
    content = response.choices[0].message.content
    token_dict = {
        "prompt_tokens": response.usage.prompt_tokens,
        "completion_tokens": response.usage.completion_tokens,
        "total_tokens": response.usage.total_tokens,
    }
    return content, token_dict

