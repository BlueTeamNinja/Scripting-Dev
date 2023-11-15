import random

def get_player_choice():
    """Asks the user to select rock, paper, or scissors and returns the choice in uppercase."""
    choice = input("(R)ock, (P)aper, or (S)cissors? ").upper()

    if choice == 'R':
        full_choice = 'ROCK'
    elif choice == 'P':
        full_choice = 'PAPER'
    elif choice == 'S':
        full_choice = 'SCISSORS'
    else:
        full_choice = choice

    print(f"You chose {full_choice.lower()}.")
    return full_choice

def get_computer_choice():
    """Randomly selects rock, paper, or scissors for the computer and returns the choice in uppercase."""
    choices = ['rock', 'paper', 'scissors']
    comp_choice = random.choice(choices)
    print(f"The computer chose {comp_choice}.")
    return comp_choice.upper()

def game_result(player_choice, computer_choice):
    """Determines the game result and returns win (1), lose (-1), or draw (0)."""
    if player_choice == computer_choice:
        print("It's a draw.")
        return 0
    elif (player_choice == "ROCK" and computer_choice == "SCISSORS") or \
         (player_choice == "PAPER" and computer_choice == "ROCK") or \
         (player_choice == "SCISSORS" and computer_choice == "PAPER"):
        print("You win!")
        return 1
    else:
        print("You lose.")
        return -1

# Python incantation
if __name__ == "__main__":
    player_choice = get_player_choice()
    computer_choice = get_computer_choice()
    game_result(player_choice, computer_choice)
