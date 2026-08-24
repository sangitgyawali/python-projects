students = []


def add_student():
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    grade = input("Enter student grade: ")

    student = {
        "name": name,
        "age": age,
        "grade": grade
    }

    students.append(student)
    print("Student added successfully!")


def show_students():
    if len(students) == 0:
        print("No students found.")
        return

    print("\n--- Student List ---")

    for i, student in enumerate(students, start=1):
        print(f"{i}. {student['name']} | Age: {student['age']} | Grade: {student['grade']}")


def search_student():
    name = input("Enter student name to search: ")

    for student in students:
        if student["name"].lower() == name.lower():
            print("\nStudent found!")
            print("Name:", student["name"])
            print("Age:", student["age"])
            print("Grade:", student["grade"])
            return

    print("Student not found.")


def delete_student():
    name = input("Enter student name to delete: ")

    for student in students:
        if student["name"].lower() == name.lower():
            students.remove(student)
            print("Student deleted.")
            return

    print("Student not found.")


def main():
    while True:
        print("\n===== STUDENT MANAGEMENT SYSTEM =====")
        print("1. Add Student")
        print("2. Show Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            show_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            delete_student()

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")


main()