# Breutzmann, Robert
# CSD 325 - Advanced Python
# Assignment 8.2 - Due Date 11/24/2025

import json

def showStudent(jsonFile):

    # Load the JSON file as a python List.
    with open(jsonFile, "r") as file:
        students = json.load(file)

        # Loop through the list and print get the information for each student's name
        for student in students:
            last = student["L_Name"]
            first = student["F_Name"]
            id = student["Student_ID"]
            email = student["Email"]

        # Create and Print the students.
            studentString = f"{last}, {first}: ID-{id}, Email- {email}"
            print(studentString)

    print("")

studentFile = "student.json"

print("This is the original list")
showStudent(studentFile)

newStudent = {
        "F_Name": "Robert",
        "L_Name": "Breutzmann",
        "Student_ID": 12345,
        "Email": "rbreutzmann@my365.bellevue.edu"
    }

with open(studentFile, "r") as file:
    students = json.load(file)

students.append(newStudent)

with open(studentFile, "w") as file:
    json.dump(students, file, indent=4)

print("This is the amended list")

showStudent(studentFile)

print("The Database has been amended")
