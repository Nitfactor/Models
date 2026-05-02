from dotenv import load_dotenv
from google import genai
from google.genai import types
import requests

load_dotenv()

client = genai.Client()

def search_call(query: str):
    url = "https://www.google.com/"
    response = requests.get(url)

tool_list = [search_call]


system_prompt = """
You have been provided with a search engine in your tools.
When the user gives you a prompt, treat that prompt as a search query.
Using the tools, you need to figure out a one line answer to the user prompt.
Give the user the answer that you have created in one line.
NOTE: No matter what the user prompts, you give the answer in the one line and onto the point.
"""

user_input = input("Your prompt: ")

response = client.models.generate_content(
    model="gemini-3-flash-preview", 
    contents=user_input,
    config=types.GenerateContentConfig(
        system_instruction=system_prompt,
        tools=tool_list,
    )
)

print(response.text)