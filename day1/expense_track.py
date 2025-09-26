def show_menu():
    """Display the menu options to the user."""
    print("\n=== Expense Tracker Menu ===")
    print("1. Add expense")
    print("2. View expenses")
    print("3. Show total")
    print("4. Exit")

def add_expense(expenses):
    '''Ask the user for expense name and amount, and store it in list.'''
    item = input("Enter expense name: ").strip()
    try:
        amount = float(input("Enter expense amount: "))
        expenses.append({"item" : item, "amount" : amount})
        print("Invalid amount! Please Enter a number.")
        
    except ValueError:
        print("Invalid amount! Please enter a number.")
        
def view_expense(expenses):
    '''Show all the expenses.'''
    if not expenses:
        print("No expeses yet.")
        return
    print("\n Your expenses:")
    for i, exp in enumerate(expenses, start = 1):
        print(f"{i}. {exp["item"]} - {exp["amount"]}")
        
def show_total(expenses):
    '''Calculate and show the total of all the expenses.'''
    total = 0
    for exp in expenses:
        total += exp["amount"]
    print(f"\n Total expenses: {total}")
    
def main ():
    '''Main program loop that controls menu and user choice.'''
    
    expenses = []
    
    while True:
        show_menu()
        choice = input("Choose an option (1-4): ").strip()
        
        match choice:
            case "1":
                add_expense(expenses)
            case "2":
                view_expense(expenses)
            case "3":
                show_total(expenses)
            case "4":
                print("GoodBye!")
                break
            case _:
                print("Please enter 1, 2, 3, or 4.")
                
if __name__ == "__main__":
    main()