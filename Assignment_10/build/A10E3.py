
"""
-------
Author: Elicia Ramitt
-------

-------------
Name of File: A10E3.py (Assignment 10 Exercise)
-------------

------------
Description: This is a guessing game with the user. The user must guess the computer's random number between 1-100
------------ 

-----
Usage: python A10E3.py
-----

-------------------------------
Command to run Script from CLI:  python A10E3.py
-------------------------------

------------------------------
Description of the Parameters: A10E3.py = this is technically the first and only parameter. This runs the program.
------------------------------
"""

# Import random
from random import randint

# main function
def main():

    # get computer guess
    magicNum = randint(1, 100)
    # Get player's guess
    playerGuess = None

    playAgain = "y"
    # While loop
    while playAgain.lower() == "y":
        
        while playerGuess != magicNum:
        # Get player's guess
            playerGuess = get_player_guess()
            
            # Call check_player_guess
            check_player_guess(magicNum, playerGuess)

        # Play again?
        playAgain = input("Play again? ")

        

# get_player_guess() function
def get_player_guess():
    # Get player's guess
    guess = int(input("What is your guess? "))

    # make sure it is valid
    if (0 < guess <= 100):
        # Return guess
        return guess
    
    # Not valid
    else:
        # Get the guess again
        print("Invalid guess. Please enter a number between 1 and 100.")
        guess = int(input())

        # Return guess
        return guess
    

# check_player_guess() function
def check_player_guess(magicNum, playerGuess):
    

    # Compare to random guess via if statement
    # Too high
    if (magicNum < playerGuess):

        # Feedback
        print("Your number is too high!")
    
    # Too low
    elif (magicNum > playerGuess):

        # Feedback
        print("Your number is too low!")
    
    # Just right
    elif (magicNum == playerGuess):

        # Feedback
        print("Congratulations! You guessed it!")

# Python Incantation
if __name__ == "__main__":
    main()