students = []

def add_student():
    name = input("Enter student name:")
    age = input("Enter student age:")
    grade = input("Enter student grade:")

    student = {
        "name" = name,
        "age" = age,
        "grade" = grade
    }

    students.append(student)
    print("Student added successfully!")