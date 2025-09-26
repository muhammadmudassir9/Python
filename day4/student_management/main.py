from mypkg.io_utils import (
    read_students_csv,
    write_students_csv,
    write_students_json,
    add_student,
    search_student,
)
from mypkg.errors import InvalidStudentError


def main():
    students = read_students_csv("data/students.csv")

    while True:
        print("\n ---Student Management System--- ")
        print("1. View all students")
        print("2. Add a student")
        print("3. Search student")
        print("4. Save and Export")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        try:
            if choice == "1":
                if not students:
                    print("No students found.")
                else:
                    for s in students:
                        print(f"- {s['Name']} (Age: {s['Age']}, Grade: {s['Grade']})")

            elif choice == "2":
                name = input("Enter name: ")
                age = input("Enter age: ")
                grade = input("Enter grade: ")
                add_student(students, name, age, grade)
                print("Student added successfully!")

            elif choice == "3":
                name = input("Enter name to search: ")
                student = search_student(students, name)
                if student:
                    print(f"Found: {student['Name']} (Age: {student['Age']}, Grade: {student['Grade']})")
                else:
                    print("Student not found.")

            elif choice == "4":
                write_students_csv("data/students.csv", students)
                write_students_json("data/students.json", students)
                print("--Data saved to CSV and JSON--")

            elif choice == "5":
                print("Exit program.")
                break

            else:
                print("Invalid choice. Please enter 1-5.")

        except InvalidStudentError as e:
            print("Data error:", e)
        except Exception as e:
            print("Unexpected error:", e)


if __name__ == "__main__":
    main()
