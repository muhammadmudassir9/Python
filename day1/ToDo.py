def show_menu():
    
    #Prints the menu otpion so the user knows what they can do.
    print("--- To Do List Menu ---")
    print("1. Add Task")
    print("2. Review Task")
    print("3. Remove Task")
    print("4. Exit")
    
def add_task(tasks):
    
    task = input("Enter a new task (or press enter to cancel): ").strip() # .strip removes the extra spaces 
    
    if task:
        tasks.append(task)
        print(f"Added: {task}")
    else:
        print("No Task added.")
        
def view_task(tasks):
    #Shows all the tasks, numbered. If no task tell the user that list is empty.
    if not tasks:
        print("your ToDo list is empty!")
        return
    print("\n Your Tasks:")
    for i, tasks in enumerate(tasks, start=1):
        print(f"{i}. {tasks}")
        
def remove_task(tasks):
    #Remove a task by its number, if you are done with your task.
    
    if not tasks:
        print("Nothing to remove.Your list is empty.")
        return
    view_task(tasks)
    
    choice = input("Enter the task number you want to remove or press 0 to cancel.").strip()
    #validate input 
    try:
        index = int(choice)
        if index == 0:
            print("Remove cancelled.")
            return
        removed = tasks.pop(index - 1)
        print(f"Removed: {removed}")
        
    except ValueError:
        print("Enter a valid number.")
    except IndexError:
        print("Task number does not exist.")
        
def main():
        #The main program loop. Keeps running untill user asks to exit.
        
        tasks = []
        while True:
            show_menu()
            choice = input("choose an option (1-4): ").strip()
            
            match choice:
                case "1":
                    add_task(tasks)
                case "2":
                    view_task(tasks)
                case "3":
                    remove_task(tasks)
                case "4":
                    print("Done!")
                    break      
                case _:
                    print("Please enter 1, 2, 3 or 4.")
                    
if __name__ == "__main__":
    main()                    
                      
                       
                
            
        
        
            