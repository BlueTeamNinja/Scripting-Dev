"""
A10E3.py: A Python script for a number guessing game.

This script allows the player to guess a random number between 1 and 100,
providing feedback and offering a replay option after each game.
"""

import random

def main():
    """
    Plays the guessing game until the player opts out.
    """
    while True:
        magic_number = random.randint(1, 100)
        while True:
            guess = get_player_guess()
            if check_player_guess(guess, magic_number):
                break

        if input("Play again? (yes/no): ").lower() != 'yes':
            break

def get_player_guess():
    """
    Asks for and validates the player's guess.

    Returns:
    int: The validated guess of the player.
    """
    while True:
        try:
            guess = int(input("Enter a guess (1-100): "))
            if 1 <= guess <= 100:
                return guess
            else:
                print("Invalid guess. Please enter a number between 1 and 100.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def check_player_guess(guess, magic_number):
    """
    Compares the guess to the magic number and prints feedback.

    Parameters:
    guess (int): The player's guess.
    magic_number (int): The number to be guessed.

    Returns:
    bool: True if the guess is correct, False otherwise.
    """
    if guess < magic_number:
        print("Too low!")
        return False
    elif guess > magic_number:
        print("Too high!")
        return False
    else:
        print("Congratulations! You guessed it!")
        return True

# Example usage
if __name__ == "__main__":
    main()
