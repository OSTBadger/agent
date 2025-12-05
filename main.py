import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import argparse
load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

# Parse command line args
parser = argparse.ArgumentParser(description="Chatbot")
parser.add_argument("prompt", type=str, help="User prompt")
parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
args = parser.parse_args()
user_prompt = args.prompt
messages = [types.Content(role="user", parts=[types.Part(text=user_prompt)])]

resp = client.models.generate_content(model="gemini-2.0-flash-001",contents=messages)
if resp.usage_metadata == None:
    raise RuntimeError("API Request Failed")
if args.verbose:
    print(f'User prompt: {user_prompt}')
    print(f"Prompt tokens: {resp.usage_metadata.prompt_token_count+1}\nResponse tokens: {resp.usage_metadata.candidates_token_count}")
    print("Response:")
print(resp.text)
