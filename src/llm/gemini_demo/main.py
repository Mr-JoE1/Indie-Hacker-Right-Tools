###
#!pip install google-cloud-aiplatform
#!pip install google-generativeai
#!pip install python-dotenv

import os
import google.generativeai as genai

# Authenticate using API key
genai.configure(api_key="")

# Create a Gemini Pro model instance
model = genai.GenerativeModel('gemini-pro')

# Define your question
prompt_parts = ["Who are you?"]

response = model.generate_content('What is AI?')
print(response.text)
