# continue updating v4 to reduce code to further functions...

# import functions from game_functions.py file/module
from game_functions import welcome_message, get_player_choice, get_computer_choice, announce_winner, write_scores_to_file

def main():
    # declare variables for counting score, set to 0 at start of play
    player_score = 0
    computer_score = 0

    # displays welcome message and retrieves the players name
    name = welcome_message()

    # main game loop
    # use a for loop to specify number of games played
    for _ in range(7):
        # use get_player_choice function to ask for player input. Returns choice and assigns to player_choice variable
        player_choice = get_player_choice()
        # returns choice and assigns to computer_choice variable
        computer_choice = get_computer_choice()

        # if statement determines the winner and updates score
        if player_choice == computer_choice:
            print(f"You both chose {player_choice}, you draw!")
        elif player_choice == "Rock":
            if computer_choice == "Scissors":
                print("Rock smashes Scissors, you win!")
                player_score += 1
            else:
                print("Paper wraps Rock, you lose!")
                computer_score += 1
        elif player_choice == "Paper":
            if computer_choice == "Rock":
                print("Paper wraps Rock, you win!")
                player_score += 1
            else:
                print("Scissors cut Paper, you lose!")
                computer_score += 1
        elif player_choice == "Scissors":
            if computer_choice == "Paper":
                print("Scissors cut Paper, you win!")
                player_score += 1
            else:
                print("Rock smashes Scissors, you lose!")
                computer_score += 1

        # display current score after each round of play
        print(f"Current Score: {name} {player_score} - Computer {computer_score}")

    # call function to announce the winner
    announce_winner(name, player_score, computer_score)

    # record the final scores to a file
    write_scores_to_file(name, player_score, computer_score)

# ensure this script runs only when executed directly, not imported
if __name__ == "__main__":
    main()
