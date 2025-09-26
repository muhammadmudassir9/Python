class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{self.owner} deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        # Default withdraw 
        if amount <= self.balance:
            self.balance -= amount
            print(f"{self.owner} withdrew {amount}. New balance: {self.balance}")
        else:
            print("Insufficient balance.")

    def show_balance(self):
        print(f"{self.owner}'s balance: {self.balance}")


# Child Class 1: SavingsAccount
class SavingsAccount(Account):
    def __init__(self, owner, balance=0, withdrawal_limit=2000):
        super().__init__(owner, balance)
        self.withdrawal_limit = withdrawal_limit  
    def withdraw(self, amount):
        if amount > self.withdrawal_limit:
            print(f"Cannot withdraw more than {self.withdrawal_limit} at once (Savings Rule).")
        elif amount <= self.balance:
            self.balance -= amount
            print(f"{self.owner} withdrew {amount}. New balance: {self.balance}")
        else:
            print("Insufficient balance.")


# Child Class 2: CurrentAccount
class CurrentAccount(Account):
    def __init__(self, owner, balance=0, overdraft_limit=5000):
        super().__init__(owner, balance)
        self.overdraft_limit = overdraft_limit  

    def withdraw(self, amount):
        if amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            print(f"{self.owner} withdrew {amount}. New balance: {self.balance}")
        else:
            print("Withdrawal exceeds overdraft limit.")



def main():
    
    ali_savings = SavingsAccount("MD", 5000)
    sara_current = CurrentAccount("AK", 2000)

    # Polymorphism in action
    accounts = [ali_savings, sara_current]

    for acc in accounts:
        acc.show_balance()    # same method, works differently depending on object type
        acc.deposit(1000)     # inherited from base class
        acc.withdraw(3000)    # overridden → behaves differently for Savings vs Current
        print("-" * 40)


if __name__ == "__main__":
    main()
