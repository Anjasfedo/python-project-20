import random  # Import the 'random' module for generating random numbers.

def rollDice():
    # Define ASCII art representations of each possible dice face.
    diceDrawing = {
        1: (
            "-----",
            "|   |",
            "| o |",
            "|   |",
            "-----",
        ),
        2: (
            "-----",
            "|o  |",
            "|   |",
            "|  o|",
            "-----",
        ),
        3: (
            "-----",
            "|o  |",
            "| o |",
            "|  o|",
            "-----",
        ),
        4: (
            "-----",
            "|o o|",
            "|   |",
            "|o o|",
            "-----",
        ),
        5: (
            "-----",
            "|o o|",
            "| o |",
            "|o o|",
            "-----",
        ),
        6: (
            "-----",
            "|o o|",
            "|o o|",
            "|o o|",
            "-----",
        ),
    }
    
    # Prompt the user if they want to roll the dice.
    roll = input("> Roll the dice? (Yes/No): ")
    
    # Continue rolling as long as the user responds with 'Yes'.
    while roll.capitalize() == "Yes":
        # Generate random numbers for two dice rolls.
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)

        # Display the result of the dice rolls and the corresponding ASCII art.
        print(f"Dice rolled: {dice1} and {dice2}")
        print("\n".join(diceDrawing[dice1]))
        print("\n".join(diceDrawing[dice2]))

        # Prompt the user if they want to roll again.
        roll = input("> Roll again? (Yes/No): ")

# Call the rollDice function to execute the dice rolling simulation.
rollDice()
