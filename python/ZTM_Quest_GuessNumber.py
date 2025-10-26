# Problem Statement: Number Guessing Game for ZTM Quest Project
# The computer selects a random number between 1 and 100. Player tries to guess it until correct.
# Time Complexity: O(N) in worst case (N = range of numbers)
# Space Complexity: O(1)

import random

def guess_number_game():
    number = random.randint(1, 100)
    attempts = 0
    guess = 0

    print("Welcome to ZTM Quest Number Guessing Game!")
    print("I have selected a number between 1 and 100. Try to guess it.")

    while guess != number:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            if guess < number:
                print("Too low! Try again.")
            elif guess > number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed it in {attempts} attempts.")
        except ValueError:
            print("Please enter a valid integer.")

# Example run
# guess_number_game()
