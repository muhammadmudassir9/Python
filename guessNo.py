import random

def guess_number():
    sec_no = random.randint(1,20)
    
attempts = 0
max_attempts = 5

print("Welcome to Guess the number Game!")
print("I am thinkng of a number betwenn 1 and 20")

while attempts< max_attempts:
    sec_no= random.randint(1,20)
    guess = int(input("Enter your guess!"))
    attempts += 1

    if guess < sec_no:
        print("Too low! try Again!")
    elif guess > sec_no:
        print("Too High! Try Again")
    else:
        print(f"Correct! The number was {sec_no}.")
        print(f"You guessed it in {attempts} attempts.")
        break   
else:
    print(f"Out of attempts! The number was {sec_no}")
    
guess_number()