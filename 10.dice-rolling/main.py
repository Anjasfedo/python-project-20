import random
def rollDice():
    roll = input("> Roll the dice? (Yes/No): ")
    
    while roll.capitalize() == "Yes":
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)

        print(f"Dice rolled: {dice1} and {dice2}")

        roll = input("> Roll again? (Yes/No): ")

rollDice()