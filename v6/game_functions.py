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


# function to determine who is winning. There are 3 possible scenarios: player wins, computer wins or draw
def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "draw"
    elif (player_choice == "Rock" and computer_choice == "Scissors") or \
            (player_choice == "Paper" and computer_choice == "Rock") or \
            (player_choice == "Scissors" and computer_choice == "Paper"):
        return "player"
    else:
        return "computer"


# Function to update the scores based on the winner of each round
def update_scores(winner, player_score, computer_score):
    if winner == "player":
        player_score += 1
    elif winner == "computer":
        computer_score += 1
    return player_score, computer_score


# Function containing the main game logic
def main_game_logic(name):  # Pass name as an argument
    player_score = 0
    computer_score = 0
    for _ in range(7):
        player_choice = get_player_choice()
        computer_choice = get_computer_choice()
        winner = determine_winner(player_choice, computer_choice)
        player_score, computer_score = update_scores(winner, player_score, computer_score)
        print(f"Current Score: {name} {player_score} - Computer {computer_score}")
        if winner == "draw":
            print(f"You both chose {player_choice}, it's a draw!")
        else:
            print(f"{winner.capitalize()} wins this round!")
    return player_score, computer_score