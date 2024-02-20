# Import necessary functions from the game_functions module
from game_functions import welcome_message, main_game_logic, announce_winner, write_scores_to_file


def main():
    # Call the welcome_message function to greet the player and get their name
    name = welcome_message()
    # Call the main_game_logic function to run the game logic and get the final scores
    player_score, computer_score = main_game_logic(name)  # Pass name as an argument
    # Call the announce_winner function to determine and display the winner of the game
    announce_winner(name, player_score, computer_score)
    # Call the write_scores_to_file function to record the final scores in a file
    write_scores_to_file(name, player_score, computer_score)


# Ensure the main function is executed only when the script is run directly, not when imported as a module
if __name__ == "__main__":
    main()

