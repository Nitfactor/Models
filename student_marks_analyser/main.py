from dotenv import load_dotenv
from google import genai
from google.genai import types
import os
import csv

load_dotenv()

client = genai.Client()

FILE_NAME = "student.csv"
HEADERS = ["Name", "Marks", "Total"]

if not os.path.isfile(FILE_NAME):
    with open(FILE_NAME, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(HEADERS)

def load_data():
     rows = []
     if os.path.exists(FILE_NAME):
          with open(FILE_NAME, 'r', newline='') as file:
               reader = csv.reader(file)
               rows = list(reader)
     return rows

def delete_data():
     data = load_data()
     students = data[1:]

     if not students:
          print("No record found")

     for i, row in enumerate(students, 1):
          print(f"{i}. {row}")

     try:
          num = int(input("Enter the number to delete: "))
          if 1 <= num <= len(students):
               removed = data.pop(num)
               with open(FILE_NAME, 'r', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerows(data)
               print(f"Successfully deleted: {removed}")
     except ValueError:
          print("Not a valid option")

# def load_data():
#      filename = []
#      if (os.path.exists(filename)):
#           with open(filename, 'w', encoding="utf-8") as file:
#                for line in file:
#                     text = line.strip().rsplit("||", 1)
# load_data(filename)

# def delete_data():
#      load_data(filename)
#      try:
#           num = (int("Enter the no: "))
#           if 1 <= num <= len(filename):
#                remove = filename.pop(num-1)
#                print(f"Data successfully deleted: {remove}")
#           else:
#                print("Invalid")
#      except ValueError:
#           print("Enter a valid number")
# delete_data()

def data_fillup():
        print("\n---Give the student data---\n")
        name = input("Name: ")
        marks = input("Marks: ")
        totalmarks = input("Total Marks: ")

        with open(FILE_NAME, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([name, marks, totalmarks])
        print(f"Successfully added: {name}")

        choice = input("Do you want to delete data? (1 for Yes, 2 for No): ")
        if choice == "1":
             delete_data()
        else:
             print("Continuing...")
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