from dotenv import load_dotenv
from google import genai
from google.genai import types
import os
import csv

load_dotenv()

client = genai.Client()

filename = "student.csv"
headers = ["Name", "Marks", "Total"]

if not os.path.isfile(filename):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(headers)

def data_fillup():
        print("\n---Give the student data---\n")
        name = input("Name: ")
        marks = input("Marks: ")
        totalmarks = input("Total Marks: ")

        with open(filename, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([name, marks, totalmarks])
        print(f"Successfully added: {name}")
data_fillup()

def get_student_data():
     try:
          with open("student.csv", 'r' ) as file:
               return file.read()
     except Exception as e:
          return f"Error reading file: {str(e)}"
     
tool_list = [get_student_data]

system_prompt = f"""
You are an analytic system. You do not have the data initially. 
If the user asks about students or marks, you MUST use the 'get_student_data' tool to see the file content.
Give the output in simple English and use tables for performance summaries.
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