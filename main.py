import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import sys


load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

try:
    user_prompt = sys.argv[1]
except:
    raise Exception("No prompt provided")

messages = [
    types.Content(role="user",
                  parts=[types.Part(text=user_prompt)])
]

response = client.models.generate_content(
    model = "gemini-2.0-flash-001",
    contents = messages
)
try: 
    verbose_flag = sys.argv[2]
    print(f"User prompt: {user_prompt}")
    # print(response.text)
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
except:
    print(response.text)