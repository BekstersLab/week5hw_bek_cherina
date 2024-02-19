# use import random for use in get_computer_choice() function
import random


def welcome_message():
    # ask for player's name and capitalize the first letter
    name = input("Hello, please enter your name: ").capitalize()
    # greet player by name and explain the game rules
    print(f"\nWelcome to Rock, Paper, Scissors {name}!")
    print("We are going to play seven games, may the best player win!")
    # return player's name to use elsewhere in program
    return name


def get_player_choice():
    # ask player for choice and capitalize first letter
    choice = input("\nChoose Rock, Paper or Scissors: ").capitalize()
    # return player's choice
    return choice


# function picks a random choice for the computer.
def get_computer_choice():
    # define choices
    items = ['Rock', 'Paper', 'Scissors']
    # select a random choice for the computer
    computer_choice = random.choice(items)
    # print the computer choice as proof
    print(f"Computer: {computer_choice}")
    # return computer's choice
    return computer_choice


def announce_winner(name, player_score, computer_score):
    # compare scores to determine outcome of game
    if player_score == computer_score:
        print("It's a draw!")
    elif player_score > computer_score:
        print(f"Congratulations, you win with a final score of {player_score}:{computer_score}")
    elif computer_score > player_score:
        print(f"Commiserations, the computer wins with a final score of {computer_score}:{player_score}")


# write scores to a file as a record of play
def write_scores_to_file(name, player_score, computer_score):
    # open game_scores.txt file in append mode to add to content (not overwrite!)
    with open('game_scores.txt', 'a') as file:
        # write final score to file
        file.write(f"Final Score: {name} {player_score} - Computer {computer_score}\n")