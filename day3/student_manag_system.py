def show_menu():
    # It will display the menue for student management system.
    print("\n--- Student Management Menu ---")
    print("1. Add student")
    print("2. Update student")
    print("3. Delete student")
    print("4. View students")
    
    print("5. Average marks")
    print("6. Exit")
    
def add_student(students):
    #Add student name and marks usding dictionary
    name = input("Enter student name: ").strip()
    if not name:
        print("Name can not be empty.")
        return  
    try:
        marks = float (input("Enter marks(number: )"))      
    except ValueError:
        print("Invalid marks.")
        return
    students.append({"name": name, "marks": marks})
    print(f"Added: {name} with marks {marks}")
 
def view_students(students):
    #Shows all students.
    if not students:
        print("No students yet!") 
        input("Enter to return to menu.") 
        return
    print("\n students: ")
    for i, s in enumerate(students, start = 1):
        print(f"{i}. {s['name']} - {s['marks']}")

    input("Press Enter to return to menu.")
    
def update_student(students):
    if not students:
        print("No student to update.")
        return
    view_students(students)
    try:
        index= int(input("Enter student number to update: "))
        if index < 1 or index > len(students):
            print("Invalid student number.")
            return
    except ValueError:
        print("Enter a valid number.")
        return
    
    student = students[index -1]
    new_name = input(f"New name (press Enter to keep '{student['name']}'): ").strip()
    if new_name:
        student['name'] = new_name
        
    new_marks = input(f"New marks(press Enter to keep {student ['marks']}): ").strip()
    if new_marks:
        try:
            student['marks'] = float(new_marks)
        except ValueError:
            print("Invlaid marks input. Marks not changed.")
            return
    print("Student Updated!")
    
def delete_student(students):
    if not students:
        print("No reccord found.")
        return 
    view_students(students)
    try:
        index = int(input("Enter student number to delete: "))
        if index < 1 or index > len(students):
            print("Invalid student number.")
            return
    except ValueError:
        print("Enter a valid number.")
        return 
    
    removed = students.pop(index - 1)
    print(f"Deleted: {removed['name']}")
    
def average_marks(students):
    if not students:
        print("no students to calculate avergae marks.")
        input("Press Enter to return to menu...")   # <-- pause so user can see the message
        return
    total = sum(s['marks'] for s in students)
    avg = total / len(students)
    print(f"Average marks: {avg:.2f}")
    input("Press enter to return  to menu.")
        
def main():
    students = []
    while True:
        show_menu()
        choice = input ("choose (1-6): ").strip()
        if choice == "1":
            add_student(students)
        elif choice == "2":
            update_student(students)
        elif choice == "3":
            delete_student(students)
        elif choice == "4":
            view_students(students)
        elif choice == "5":
            average_marks(students)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Please choose a valid option 1-6.")
            
            
if __name__ == "__main__":
    main()