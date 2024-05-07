#importing random module 
import random
# import logging module
import logging
from art import welcome_message

# Configure the logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# define game funtion
def game():
    # Generate a random number between 0 and 100
    computer_number = random.randint(0, 100)
    # Define a list of valid difficulty levels
    valid_difficulties = ['easy', 'hard']

    # Initialize the variable diff and continue loop until valid difficulty is chosen
    diff = ""
    while diff not in valid_difficulties:
        # Prompt user for difficulty choice
        diff = input("Choose difficulty 'easy' or 'hard': ").lower()
        if diff not in valid_difficulties:
            # If input is not valid, print error message
            logger.info("Invalid input. Please choose 'easy' or 'hard'.")

    # Print message indicating the range of guess
    logger.info("I am thinking of a number between 0 and 100.")
    # Initialize variable to store number of attempts
    attempts = 0

    # If difficulty is easy, set attempts to 10; if difficulty is hard, set attempts to 5
    if diff == "easy":
        attempts = 10
    elif diff == "hard":
        attempts = 5

    # Print number of attempts available
    logger.info(f"You have {attempts} attempts to guess the number.")

    # Initialize variable to control game loop
    end_of_game = False


    # Start the game loop
    while not end_of_game:
        # Prompt user to input their guess and convert to integer
        guess = int(input("Guess the number: "))
        # Decrement the number of attempts remaining
        attempts -= 1

        # If the guess is correct
        if guess == computer_number:
            # Print a message indicating the correct guess
            logger.info(f"{guess} is the correct answer.")
            # Set end_of_game flag to True to end the game
            end_of_game = True
        # If the guess is too low
        elif guess < computer_number:
            # Print a message indicating the guess is too low
            logger.info(f"{guess} is too low. You have {attempts} attempts left.")
        # If the guess is too high
        else:
            # Print a message indicating the guess is too high
            logger.info(f"{guess} is too high. You have {attempts} attempts left.")

        # If there are no attempts left or the game is not over yet, prompt the user to guess again
        if attempts == 0:
            end_of_game = True
        elif not end_of_game:
            logger.info("Guess again!")

    # Ask user if they want to play again
    play_again = input("Do you want to play again? (yes/no): ").lower()
    # If user wants to play again, call the game function recursively to start a new game
    if play_again == "yes":
        game()

# Start the game
logger.info(welcome_message)
game()