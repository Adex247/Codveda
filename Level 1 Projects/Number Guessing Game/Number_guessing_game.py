"""
Task 2: Number Guessing Game

Description:
    Randomly generates a number between 1 and 100. The user has to guess
    the number, and the program gives feedback if the guess is too high
    or too low.

Objectives covered:
    - Use the random module to generate a random number.
    - Give the user multiple attempts to guess the number.
    - Provide appropriate feedback ("Too high" / "Too low").
    - Exit the game if the user guesses correctly or after a maximum
      number of attempts.
"""

import random


def play_game(max_attempts=7):
    secret_number = random.randint(1, 100)
    attempts_used = 0

    print("I'm thinking of a number between 1 and 100.")
    print(f"You have {max_attempts} attempts to guess it.\n")

    while attempts_used < max_attempts:
        guess_str = input(f"Attempt {attempts_used + 1}/{max_attempts} - Enter your guess: ")

        # Validate the input is a number
        if not guess_str.strip().lstrip("-").isdigit():
            print("Please enter a valid whole number.\n")
            continue

        guess = int(guess_str)
        attempts_used += 1

        if guess < 1 or guess > 100:
            print("Your guess should be between 1 and 100.\n")
            continue

        if guess < secret_number:
            print("Too low!\n")
        elif guess > secret_number:
            print("Too high!\n")
        else:
            print(f"Correct! You guessed it in {attempts_used} attempt(s).")
            return

    print(f"Sorry, you've used all {max_attempts} attempts. "
          f"The number was {secret_number}.")


def main():
    play_game()

    while True:
        again = input("\nPlay again? (y/n): ").strip().lower()
        if again == "y":
            print()
            play_game()
        elif again == "n":
            print("Thanks for playing!")
            break
        else:
            print("Please enter 'y' or 'n'.")


if __name__ == "__main__":
    main()