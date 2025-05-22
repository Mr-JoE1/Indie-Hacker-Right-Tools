from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
STEP_API_KEY=os.getenv("STEP_API_KEY")
client = OpenAI(api_key=STEP_API_KEY, base_url="https://api.stepfun.com/v1")
 
completion = client.chat.completions.create(
	model="step-1-8k",
	messages=[
		{
			"role": "system",
			"content": "You are an AI chat assistant provided by StepFun. You are good at conversations in Chinese, English, and many other languages. While ensuring the security of user data, you can provide fast and accurate answers to user questions and requests. At the same time, your answers and suggestions should reject content related to pornography, gambling, drugs, and violent terrorism.",
		},
		{"role": "user", "content": "Hello, please introduce StepFun's artificial intelligence!"},
	],
)
 
print(completion.choices[0].message.content)
