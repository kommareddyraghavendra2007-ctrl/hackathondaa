import random

# Computer chooses a random number between 1 and 100
number = random.randint(1, 100)

print("Welcome to the Number Guessing Game!")
print("I have chosen a number between 1 and 100.")

# Keep asking until the user guesses correctly
while True:
    guess = int(input("Enter your guess: "))

    # Check if the guess is too high
    if guess > number:
        print("Too High! Try again.")

    # Check if the guess is too low
    elif guess < number:
        print("Too Low! Try again.")

    # The guess is correct
    else:
        print("Correct! You guessed the number!")
        break