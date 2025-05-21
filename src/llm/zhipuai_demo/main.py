#!pip install zhipuai
from zhipuai import ZhipuAI

def main():
    client = ZhipuAI(api_key="") # Fill in your own APIKey
    response = client.chat.completions.create(
        model="glm-4",  # Fill in the name of the model to be called
        messages=[
            {"role": "user", "content": "Hello"},
            {"role": "assistant", "content": "I am an artificial intelligence assistant"},
            {"role": "user", "content": "What is your name"},
            {"role": "assistant", "content": "My name is chatGLM"},
            {"role": "user", "content": "What can you do"}
        ],
    )
    print(response.choices[0].message.content)

if __name__ == "__main__":
  main()