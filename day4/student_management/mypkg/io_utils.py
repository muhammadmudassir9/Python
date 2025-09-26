import csv
import json
from .errors import InvalidStudentError


def read_students_csv(path):
    """Read students from CSV and validate them."""
    students = []
    try:
        with open(path, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for i, row in enumerate(reader, start=1):
                if not row.get("Name") or not row.get("Age") or not row.get("Grade"):
                    raise InvalidStudentError(f"Row {i} has missing fields: {row}")
                try:
                    row["Age"] = int(row["Age"])
                except ValueError:
                    raise InvalidStudentError(f"Row {i} has invalid Age: {row['Age']}")
                students.append(row)
    except FileNotFoundError:
        # if file not found, return empty list
        return []
    return students


def write_students_csv(path, students):
    """Save students back to CSV file."""
    with open(path, "w", newline="", encoding="utf-8") as f:
        fieldnames = ["Name", "Age", "Grade"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(students)


def write_students_json(path, students):
    """Write students to JSON file."""
    with open(path, "w", encoding="utf-8") as f:
        json.dump(students, f, indent=2, ensure_ascii=False)


def add_student(students, name, age, grade):
    """Add a new student to the list."""
    try:
        age = int(age)  # validate age
    except ValueError:
        raise InvalidStudentError("Age must be a number.")
    new_student = {"Name": name, "Age": age, "Grade": grade}
    students.append(new_student)


def search_student(students, name):
    """Search student by name."""
    for student in students:
        if student["Name"].lower() == name.lower():
            return student
    return None
