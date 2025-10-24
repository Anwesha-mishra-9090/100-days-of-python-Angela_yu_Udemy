from random import randint
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

# Function to check user's guess against actual answer
def check_answer(user_guess, actual_answer, turns):
    """Checks answer against guess, returns the number of turns remaining."""
    if user_guess > actual_answer:
        print("📈 Too high.")
        return turns - 1
    elif user_guess < actual_answer:
        print("📉 Too low.")
        return turns - 1
    else:
        print(f"🎉 You got it! The answer was {actual_answer} 🎉")
        return turns

# Function to set difficulty
def set_difficulty():
    while True:
        level = input("🎯 Choose a difficulty. Type 'easy' or 'hard': ").lower()
        if level == "easy":
            return EASY_LEVEL_TURNS
        elif level == "hard":
            return HARD_LEVEL_TURNS
        else:
            print("❗ Invalid input. Please type 'easy' or 'hard'.")

# The main game function

def game():
    print("""
    █▄█ █▀█ █▀█ █▀▀ █▀█   █▀▀ █░█ █▀▀ █▀▀ █ █▄░█ █▀▀
    ░█░ █▄█ █▀▄ ██▄ █▀▄   █▄█ █▄█ ██▄ █▄█ █ █░▀█ ██▄

       > INITIATING SECURE NUMBER GUESSING PROTOCOL...
       > TARGET RANGE: 1 - 100
       > DIFFICULTY LEVEL: [ EASY | HARD ]
       > TRACE STATUS: UNDETECTED ☠
       > ENCRYPTED GUESS SEQUENCE STARTED...
        """)

    print(logo)
    print("🎮 Welcome to the Number Guessing Game!")
    print("🔢 I'm thinking of a number between 1 and 100.")

    answer = randint(1, 100)
    turns = set_difficulty()

    guess = None
    while guess != answer:
        if turns == 0:
            print("💀 You've run out of guesses. You lose.")
            print(f"The correct number was: {answer}")
            break

        print(f"\n🕐 You have {turns} attempt(s) remaining.")
        try:
            guess = int(input("💭 Make a guess: "))
        except ValueError:
            print("❗ Please enter a valid number.")
            continue

        turns = check_answer(guess, answer, turns)

        if guess != answer and turns > 0:
            print("🔁 Guess again.")

# Start the game
game()
