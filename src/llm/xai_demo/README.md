# simplellm
A script for using various LLMs around the world

# Overview
 - For members, everyone can get a $25 API usage credit per month.

Here is a simplified description of how to apply for and use an x.ai (Grok) API key:

### Apply for API Key

#### Prerequisites
You need to subscribe to X platform's **Premium+ membership** (monthly fee is about 1,960 yen).

#### Steps
1. Visit Grok's PromptIDE platform
   - Open the ide.x.ai website and log in
   - Click the profile icon in the upper right corner and select "API Keys"

2. Create a new API key
   - Click "Create API Key"
   - Set permissions (such as chat read, write permissions, etc.)

3. Save the API key
   - After setting the permissions, click "Save" and copy the key, save it securely

### Use API Key
 - You can reuse OpenAI's SDK.
```
from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()
client = OpenAI(api_key=os.getenv("X_AI_KEY"),base_url="https://api.x.ai/v1")
completion = client.chat.completions.create(
    model="grok-beta",
    messages=[
        {"role": "user", "content": "write a haiku about ai"}
    ]
)

print(completion.choices[0].message.content)