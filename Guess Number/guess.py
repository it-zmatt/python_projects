import random

def guess():
    x = int(input("Enter a number greater than 2: "))
    random_number = random.randint(1,x)
    guess = int(input(f"Guess the number between 1 and {x}: "))
    while guess != random_number:
        if guess < random_number:
           guess = int(input(f"Guess again, the number is HIGHER: "))
        else:
            guess = int(input(f"Guess again, the number is LOWER: ")) 
    
    if guess == random_number:
        print("Yaay! Congrats, You got it right.")

guess()


