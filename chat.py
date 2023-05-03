import os
import openai
from dotenv import load_dotenv

def configure():
    load_dotenv()

def main():
    openai.api_key = os.getenv('api_key')
    messages = []

    while True:
        content = input("User: ")
        if content:
            messages.append(
                {"role": "user", "content": content}
            )
            completion = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=messages
            )

        reply_content = completion.choices[0].message.content
        print(f'ChatGPT: {reply_content}')
        messages.append({"role": "system", "content": reply_content})

main()