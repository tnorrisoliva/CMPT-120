import random

# Global variable
player_name = ""
#variables
health = 100
inventory = ["laptop", "Books", " campus Map"]
enemies = ["Rude RA", "Dragon with a backpack", "Witch of the library","professor"]

# Function to get player's name
def get_player_name():
    global player_name
    player_name = input("Welcome to the Adventure Game! Enter your name: ")


# Function to introduce the game
def introduction():
    print(f"Hello, {player_name}! You have arrived on campus for your first year at college. Your acedemic adventure begins now.")


# Function for the main game loop
def adventure_game():

    #health = 100
    #inventory = ["Sword", "Health Potion", "Map"]
    #enemies = ["Goblin", "Dragon", "Witch"]

    # Main game loop
    while health > 0:
        print("\n--- Options ---")
        print("1. Explore")
        print("2. Check Inventory")
        print("3. Quit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            explore()
        elif choice == "2":
            check_inventory()
        elif choice == "3":
            print("Thanks for playing! Goodbye.")
            break
        else:
            print("Invalid choice. Try again.")


# Function for the exploration part of the game
def explore():
    global player_name
    print(f"\n{player_name}, you venture into the unknown")

    # Randomly encounter an enemy
    enemy = random.choice(enemies)
    print(f"Uh-oh! You encounter a {enemy}!")

    # Fight or flee
    action = input("Do you want to fight (F) or flee (L)? ").upper()

    if action == "F":
        print(f"You bravely fight the {enemy} and emerge victorious!")
        print("health=", health)
    elif action == "L":
        print(f"You wisely flee from the {enemy}. Live to learn another day!")
        print("health=",health)
    else:
        print(f"Invalid choice. You hesitate and the {enemy} attacks!")



# Function to check player's inventory
def check_inventory():
    global player_name
    print(f"\n{player_name}'s Inventory:")
    for item in inventory:
        print(f"- {item}")


# Main program
if __name__ == "__main__":
    get_player_name()
    introduction()
    adventure_game()
