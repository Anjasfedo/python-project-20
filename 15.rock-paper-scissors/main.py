import random

is_exit = False

user_points = 0
computer_points = 0

def print_input(user_input, computer_input):
    print(f"Your input is {user_input}")
    print(f"Computer input is {computer_input}")

while is_exit == False:
    options = ["rock", "paper", "scissors"]

    user_input = input("> Choose rock, paper, scissors or exit: ").lower()

    computer_input = random.choice(options)
    
    if user_input not in options and user_input != "exit":
        print("Invalid input")
    
    if user_input == "exit":
        print("Game ended")
        print(f"You got {user_points} points")
        print(f"Computer got {computer_points} points")
        is_exit = True
        
    if user_input == "rock":
        if computer_input == "rock":
            print_input(user_input=user_input, computer_input=computer_input)
            print("It is a tie")
        elif computer_input == "paper":
            print_input(user_input=user_input, computer_input=computer_input)
            print("Computer win")
            computer_points += 1
        elif computer_input == "scissors":
            print_input(user_input=user_input, computer_input=computer_input)
            print("You win")
            user_points += 1
    elif user_input == "paper":
        if computer_input == "paper":
            print_input(user_input=user_input, computer_input=computer_input)
            print("It is a tie")
        elif computer_input == "scissors":
            print_input(user_input=user_input, computer_input=computer_input)
            print("Computer win")
            computer_points += 1
        elif computer_input == "rock":
            print_input(user_input=user_input, computer_input=computer_input)
            print("You win")
            user_points += 1
    elif user_input == "scissors":
        if computer_input == "scissors":
            print_input(user_input=user_input, computer_input=computer_input)
            print("It is a tie")
        elif computer_input == "rock":
            print_input(user_input=user_input, computer_input=computer_input)
            print("Computer win")
            computer_points += 1
        elif computer_input == "paper":
            print_input(user_input=user_input, computer_input=computer_input)
            print("You win")
            user_points += 1
