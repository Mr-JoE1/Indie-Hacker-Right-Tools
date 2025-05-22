from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()
client = OpenAI(
    api_key= os.getenv('QWENKEY'),  # Replace with the real DashScope API_KEY
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",  # Fill in the DashScope service endpoint
)

def streamResult():
    completion = client.chat.completions.create(
        model="qwen-plus",
        messages=[
            {
                'role': 'system',
                'content': 'You are a helpful assistant.'
            },
            {
                'role': 'system',
                'content': 'Large language models (LLMs) have revolutionized the field of artificial intelligence, making natural language processing tasks previously considered unique to humans possible...'
            },
            {
                'role': 'user',
                'content': 'What is the article about?'
            }
        ],
        stream=True
    )
    for chunk in completion:
        if chunk.choices[0].delta.content is not None:
            print(chunk.choices[0].dict())

def simpleResult():
    completion = client.chat.completions.create(
        model="qwen-long",
        messages=[
            {
                'role': 'system',
                'content': 'You are a helpful assistant.'
            },
            {
                'role': 'user',
                'content': 'Who are you?'
            },
        ]
    )
    print(completion.choices[0].message.content)

def main():
    streamResult()
    simpleResult()

if __name__ == "__main__":
  main()