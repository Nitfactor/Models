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

system_prompt = f"""
You are an analytic system that summarises and gives output after reading the csv file from the location - student_marks_analyser.py/student.csv
You read the file for the data. User would just use one prompt stating what he wants exactly and based on the data you give a desired output.
You give the output in simple english and if neccessary, tables.
"""

user_input = input("Your prompt: ")

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=user_input,
    config=types.GenerateContentConfig(
        system_instruction=system_prompt
    )
)

print(response.text)

# Create a Python program that allows a user to input student names along with their marks and then calculates useful statistics.

# Your program should:
# 1. Let the user input multiple students with their marks (name + integer score).
# 2. After input is complete, display:
#    - Average marks
#    - Highest marks and student(s) who scored it
#    - Lowest marks and student(s) who scored it
#    - Total number of students