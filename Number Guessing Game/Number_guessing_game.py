"""
Number Guessing Game
---------------------
A simple command-line game where the player must guess
a randomly chosen number between 1 and 100.
"""

import random

def get_user_guess() -> int:
    """Prompt the user for a valid guess between 1 and 100."""
    while True:
        try:
            guess = int(input("Insert your guess (1-100): "))
            if 1 <= guess <= 100:
                return guess
            else:
                print("Please enter a number between 1 and 100.")
        except ValueError:
            print("Invalid input. Only numbers are allowed.")


def play_game() -> None:
    """Run the main guessing game loop."""
    secret_number = random.randint(1, 100)
    print("Welcome to the Number Guessing Game!")
    print("Try to guess the secret number between 1 and 100.\n")

    while True:
        guess = get_user_guess()

        if guess > secret_number:
            print("Too high. Try again!\n")
        elif guess < secret_number:
            print("Too low. Try again!\n")
        else:
            print(f"Congratulations! You guessed it: {secret_number}")
            break

if __name__ == "__main__":
    play_game()
