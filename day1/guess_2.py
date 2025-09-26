import random

def guess_number():
    while True:
        secret_no = random.randint(1,15)
        attempts = 0
        max_attempts = 5
        
        print("\n welcome to Guess the Number Game!")
        print("I am thinking of a number between 1 and 15")
        print(f"You have maximum {max_attempts} attempts!")
        
        while attempts < max_attempts:
            guess = int(input("Enter your guess : "))
            
            attempts += 1
            
            if guess < secret_no:
                print("Too low! Try Again!")
            elif guess > secret_no:
                print("Too High! Try Again!")
            else:
                print(f"Correct! The number was {secret_no}.")
                print(f"You guessed it in {attempts} attempts.")
                break
        else:
            print(f"Out of attempts.The secret number was {secret_no}.")    
        
        play_again = input("Do you want to play again? (yes/no):").lower()
        if play_again != "yes":
            print("Thanks for playing!")
            break        
        
guess_number()

            
        
