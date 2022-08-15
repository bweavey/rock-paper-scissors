# Provides the main code flow for rock-paper-scissors.
# rps/rps.py

import sys
import random

from rps import art, text

def main():
    print(art.banner)
    input("Press Enter to continue.")
    print(text.welcome_msg)
    print(text.help_msg)
    while True:
        user_choice = None
        while user_choice == None:
            user_input = input("go on, choose: ")
            user_choice = parse_input(user_input)
        computer_choice = get_choice()

        print(f"You chose: {user_choice}")
        print(art.choice_art[user_choice])
        print(f"Computer chose: {computer_choice}")
        print(art.choice_art[computer_choice])

        results = compare_choices(user_choice, computer_choice)
        declare_outcome(results)

    print("I guess the game is over.")

def parse_input(user_input):
    if "quit" in user_input:
        end_game()
    elif "help" in user_input:
        print(text.help_msg)
        return None
    elif user_input.lower() not in ["rock", "paper", "scissors"]:
        return "invalid"
    return user_input.lower()

def get_choice():
    return ["rock", "paper", "scissors"][random.randint(0,2)]

def compare_choices(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif user_choice == "rock":
        if computer_choice == "paper":
            return "loss"
        elif computer_choice == "scissors":
            return "win"
    elif user_choice == "paper":
        if computer_choice == "scissors":
            return "loss"
        elif computer_choice == "rock":
            return "win"
    elif user_choice == "scissors":
        if computer_choice == "rock":
            return "loss"
        elif computer_choice == "paper":
            return "win"
    else:
        return "invalid"

def declare_outcome(results):
    if results == "tie":
        print("You tied, could be worse.")
    elif results == "loss":
        print("You lost, better luck next time.")
    elif results == "win":
        print("You won, well done!")
    elif results == "invalid":
        print("Trying to flip the board, are we?")

def end_game():
    print("I suppose the game is over, then. Until next time!")
    sys.exit()
