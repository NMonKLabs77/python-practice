# Algorithms Friday

print("Welcome guys! First we will practice algorithms")

# Firstly, an algorithm is step by step instructions to be run in a certain order

# Build a cake recipe excercise with functions, variables ,conditionals

# List of steps:

# Step 1: Define our Function

def make_cake(flour, eggs, butter, sugar, salt, milk, bakingsoda):
    """This function makes a cake recipe for a beginner."""
    # Step 2: Make a list of our ingredients and store it in a variable 
    ingredients = ['flour', 'eggs', 'butter', 'sugar', 'salt', 'milk', 'bakingsoda']

    # Create a loop that checks if each ingredient is in the list and provides the corresponding recipe step
    for ingredient in ingredients:
        if ingredient == 'flour' and flour:
            print("Add 2 lbs of flour")
        elif ingredient == 'eggs' and eggs:
            print("Add 3 eggs!")
        elif ingredient == 'butter' and butter:
            print("Add 2 spoons of butter")
        elif ingredient == 'sugar' and sugar:
            print("Add 3 spoons of sugar, add more to your taste preference")
        elif ingredient == 'salt' and salt:
            print("Add 2 pinches of salt")
        elif ingredient == 'milk' and milk:
            print("Pour in a glass of milk")
        elif ingredient == 'bakingsoda' and bakingsoda:
            print("Put in a pinch of baking soda")
        else:
            print(f"You are missing {ingredient} in your ingredients list")

# Prompt the user for ingredient availability
flour = input("Do you have flour? (yes/no): ").lower() == 'yes'
eggs = input("Do you have eggs? (yes/no): ").lower() == 'yes'
butter = input("Do you have butter? (yes/no): ").lower() == 'yes'
sugar = input("Do you have sugar? (yes/no): ").lower() == 'yes'
salt = input("Do you have salt? (yes/no): ").lower() == 'yes'
milk = input("Do you have milk? (yes/no): ").lower() == 'yes'
bakingsoda = input("Do you have baking soda? (yes/no): ").lower() == 'yes'

# Call the make_cake function with the user's ingredient availability
make_cake(flour, eggs, butter, sugar, salt, milk, bakingsoda)

print("You have completed the recipe!")

