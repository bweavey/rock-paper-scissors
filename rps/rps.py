# Provides the main code flow for rock-paper-scissors.
# rps/rps.py

import random

def main():
    print("Rock-paper-scissors called, choose rock, paper, or scissors.")
    user_input = input("go on, choose: ")
    user_choice = parse_input(user_input)
    computer_choice = get_choice()

    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    results = compare_choices(user_choice, computer_choice)
    declare_outcome(results)

def parse_input(user_input):
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
        print("You tied, how exciting")
    elif results == "loss":
        print("You lost, how expected")
    elif results == "win":
        print("You won, how surprising")
    elif results == "invalid":
        print("Trying to flip the board, are we?")
