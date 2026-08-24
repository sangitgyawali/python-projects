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

def show_students():
    if len(students) == 0:
        print("No students found.")
    return

    print("\n--- Student List ---")

    for i, student in enumerate(student, start=1):
        print(f"{i}. {student['name']} | Age: {student['age']} | Grade: {student['grade']}")

def search_students():
    name = input("Enter student name to search:")

    for student in students:
        if student["name"].lower() == name.lower():
            print("\nStudent found!")
            print("Name:", student["name"])
            print("Age:", student["age"])
            print("Grade:", student["grade"])
            return 

    print("Student not found.")

def delete_students():
    name = input("Enter student name to delete:")

    for student in students:
          if student["name"].lower() == name.lower():
            students.remove(student)
            print("Student deleted.")
            return

    print("Student not found.")