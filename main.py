import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
from functions.files_info import get_files_info
from prompts import system_prompt
from call_function import available_functions, call_function
import sys



def main():

    load_dotenv()
    verbose = "--verbose" in sys.argv
    args = [arg for arg in sys.argv[1:] if not arg.startswith("--")]

    if not args:
        print("AI Code Assistant")
        print("\nUsage: python main.py 'your prompt here' [--verbose]")
        print("Example: python main.py 'How do I calculate the sqaure root of 76?'")
        sys.exit(1)

    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    user_prompt = " ".join(args)

    if verbose:
        print(f"User prompt: {user_prompt}\n")

    messages = [
    types.Content(role="user",
                  parts=[types.Part(text=user_prompt)])
    ]

    generate_content(client, messages, verbose)


def generate_content(client, messages, verbose):
    max_iterations = 20
    
    for iteration in range(max_iterations):
        try:
            response = client.models.generate_content(
                model="gemini-2.0-flash-001",
                contents=messages,
                config=types.GenerateContentConfig(
                    tools=[available_functions], system_instruction=system_prompt
                ),
            )

            if verbose:
                print("Prompt tokens:", response.usage_metadata.prompt_token_count)
                print("Response tokens:", response.usage_metadata.candidates_token_count)

            # Add model's response to conversation
            for candidate in response.candidates:
                messages.append(candidate.content)

            # Check if model has final response text (no function calls)
            if response.text and not response.function_calls:
                print("Final response:")
                print(response.text)
                return response.text

            # Handle function calls if present
            if response.function_calls:
                function_responses = []

                for function_call_part in response.function_calls:
                    function_call_result = call_function(function_call_part, verbose)

                    if (
                        not function_call_result.parts
                        or not function_call_result.parts[0].function_response
                    ):
                        raise Exception("empty function call result")
                    
                    if verbose:
                        print(f"-> {function_call_result.parts[0].function_response.response}")
                    function_responses.append(function_call_result.parts[0])

                if not function_responses:
                    raise Exception("no function responses generated, exiting.")

                # Add tool responses to conversation
                tool_content = types.Content(role="tool", parts=function_responses)
                messages.append(tool_content)
            
        except Exception as e:
            print(f"Error in iteration {iteration + 1}: {e}")
            break
    
    print(f"Reached maximum iterations ({max_iterations}) without completion.")





if __name__=="__main__":
    main()






