# Rock-Paper-Scissors Game
import random


while True:
    possible_options = ["R", "P", "S"]
    user_action = input("Please enter an option ('R', 'P', or 'S'): ").upper()
    if user_action not in possible_options:
        print("Invalid input!")
    else:
        computer_action = random.choice(possible_options)
        print(f"\nPlayer ({user_action}) : CPU ({computer_action}).\n")
        if user_action == computer_action:
            print(f"Both players selected {user_action}. It's a tie!")
        elif user_action == "R":
            if computer_action == "S":
                print("Rock smashes scissors! You win!")
            else:
                print("Paper covers rock! You lose.")
            play_again = input("Play again? (y/n): ")
            if play_again.lower() != "y":
                break
        elif user_action == "P":
            if computer_action == "R":
                print("Paper covers rock! You win!")
            else:
                print("Scissors cuts paper! You lose.")
            play_again = input("Play again? (y/n): ")
            if play_again.lower() != "y":
                break
        elif user_action == "S":
            if computer_action == "P":
                print("Scissors cuts paper! You win!")
            else:
                print("Rock smashes scissors! You lose.")
            play_again = input("Play again? (y/n): ")
            if play_again.lower() != "y":
                break
            