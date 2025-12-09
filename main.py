import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
from prompts import system_prompt
import argparse
from functions.get_files_info import schema_get_files_info
from functions.get_file_contents import schema_get_files_content
from functions.write_file import schema_write_file
from functions.run_python_file import schema_run_python_file
from functions.call_function import call_function

def main():
    # Load api key from env file and connect client ,https://ai.google.dev/gemini-api/docs/api-key
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    # Provide the function calls definitions
    available_functions = types.Tool(
        function_declarations=[schema_get_files_info,schema_run_python_file,schema_write_file,schema_get_files_content],
        
    )
    # Parse command line args
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()
    user_prompt = args.prompt
    messages = [types.Content(role="user", parts=[types.Part(text=user_prompt)])]

    # Send request to Gemini
    resp = client.models.generate_content(model="gemini-2.5-flash-lite",
                                        contents=messages,
                                        config=types.GenerateContentConfig(system_instruction=system_prompt,tools=[available_functions]))
    if resp.usage_metadata == None:
        raise RuntimeError("API Request Failed")
    if args.verbose:
        print(f'User prompt: {user_prompt}')
        print(f"Prompt tokens: {resp.usage_metadata.prompt_token_count+1}\nResponse tokens: {resp.usage_metadata.candidates_token_count}")
        print("Response:")
    #Print function calls
    if len(resp.function_calls):
        contents = []
        for item in resp.function_calls:
            # Run the actual function
            content = call_function(item)
            if content.parts[0].function_response.response:
                contents.append(content)
                if args.verbose:
                    print(f"-> {content.parts[0].function_response.response}")
            else:
                raise Exception('No parts')

    print(resp.text)

    
if __name__ == "__main__":
    main()

