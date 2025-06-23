import os
from google import genai
from dotenv import load_dotenv
import sys
from google.genai import types


def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    # Checks if a prompt was given by user in terminal
    if len(sys.argv) < 2:
        print("Usage: python3 main.py 'Your prompt here'")
        sys.exit(1)

    user_prompt = sys.argv[1]

    # Checks for --verbose flag
    verbose = "--verbose" in sys.argv

    # Stores previous prompts as a list
    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    # AI response to the prompt
    response = client.models.generate_content(
        model='gemini-2.0-flash-001', 
        contents=messages
    )

    if verbose:
        print(f"User prompt: '{user_prompt}'")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Repsonse tokens: {response.usage_metadata.candidates_token_count}")
    
    print(f"Response: {response.text}")

if __name__== "__main__":
    main()