from openai import OpenAI
import json

client = OpenAI(
    api_key="AIzaSyBeJc4bXpp2hoAtjywkEgAyhKoK7DNc82Q",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

System_Prompt = """
You are a senior software engineer.

"""

prompt_text = f"""
Below is the performance data for Virat Kohli's last 33 matches and other data:
{json.dumps({}, indent=2)}

Based on this trend, his scoring consistency, and recent run rate, 
predict how many runs he will score in the next match. 
Provide a specific number and a short reason for your prediction.
"""

response = client.chat.completions.create(
    model="gemini-3-flash-preview",
    messages=[
        {"role": "system", "content": System_Prompt},
        {"role": "user", "content": prompt_text}
    ]
)

print(response.choices[0].message.content)