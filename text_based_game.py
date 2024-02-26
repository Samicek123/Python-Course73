import time
import random
#Define a Player class to store player information
class Player:
    def __init__(self):
        self.health = 100
        self.weapon = None
        self.armor = None


#Define a creature class for enemies
class Creature:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage

#Create instances of Player and Creature
player = Player()
wolf = Creature("wolf", 30, 10)
spider = Creature("Giant spider", 40, 15)

def intro():
    print("Welcome to the Text adventure game you CUNT :).")
    time.sleep(1)
    print("You find yourself in a dark and eerie forest.")
    time.sleep(1)
    print("Your goal is to find a treasure hidden n the heart of the forrest.")
    time.sleep(1)
    print("but be carefull adventurer the forest is filled with dangerous creatures.")


def make_choice(choices):
    print("Choose your path:")
    for i, choice in enumerate(choices, start=1):
        print(f"{i}, {choice}")

    while True:
        try:
            choice = int(input("Enter the number of your choice: "))
            if 1 <= choice<= len(choices):
                return choice
            else:
                print("invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def forest_path():
    print("You start walking on a narrow path trough the forest.")
    time.sleep(1)
    print("Suddenly, you incounter a fork in the road.")
    time.sleep(1)
    choices = ["Take the left path", "Take the right path"]
    choice = make_choice(choices)
    if choice == 1:
        print("You've chosen the left path.")
        time.sleep(1)
        print("As you walk, you encounter a friendly squirrel.")
        time.sleep(1)
        return True
    else:
        print("You chose to take the right path.")
        time.sleep(1)
        print("You encounter a group of aggressive wolves.")
        time.sleep(1)
        print("You manage to scare them away using a loud noise.")
        #Player collects a basic weapon after scaring away wolves
        player.weapon = "wooden Sword"
        print(f"You found a {player.weapon}")
        return True
def cave():
    print("You arrive at the entrance of a dark cave.")
    time.sleep(1)
    print("It seems to  be only way to reach the treasure.")
    time.sleep(1)

    while True:
        print("As yu enter the cave, you hear strange noises.")
        time.sleep(1)
        choices = ["Enter the left tunnel", "Enter the right tunnel"]
        choice = make_choice(choices)
        if choice == 1:
            print("You chose to enter the left tunnel.")
            time.sleep(1)
            print("You encountered a giant spider!")
            """Combat the spider"""
            combat(spider)
            return True
        else:
            print("You chose to enter the right tunnel.")
            time.sleep(1)
            print("The tunnel leads to a dead end. You backtrack to the entrance.")
            print("You need to find the correct path in the cave to reach the treasure. Try again.")
        
def treasure_room():
    print("Congratulations! You have reached the treasure room.")
    time.sleep(1)
    print("You open the treasure chest and file heaps of gold shuit Cunt")
    time.sleep(1)
    print("You have successfully completed the adventure!")


def combat(enemy):
    print (f"You are in combat with {enemy.name}!")

    while player.health > 0 and enemy.health > 0:
        print("\nPlayer stats:")
        print(f"Health: {player.health}")
        print(f"Weapon: {player.weapon}")

        print(f"\n{enemy.name} Stats:")
        print(f"Health: {enemy.health}")
        print(f"Damage: {enemy.damage}")

        attack_choice = make_choice(["Attack", "Run"])

        if attack_choice == 1:
            """Player attacks the enemy"""
            player_attack = random.randint(5, 15)
            enemy.health -= player_attack
            print(f"You attack the {enemy.name} and deal {player_attack} damage!")

            """ Enemy attacks the player """
            enemy_attack = random.randint(5, 15)
            player.health -= enemy_attack
            print(f"The {enemy.name} attacks you and deals {enemy_attack}!")
        else:
            print(f"You try to run from the {enemy.name}, but it catches you!")
            enemy_attack = random.randint(5, 15)
            player.health -= enemy_attack
            print(f"The {enemy.name} attacks you and deals {enemy_attack} damage!")
    if player.health <= 0:
        print("You have been defeated. Game over.")
        exit()
    else:
        print(f"You defeated the {enemy.name}!")

if __name__ == "__main__":
    intro()

    if forest_path():
        while not cave():
            pass #Loop until the player finds the correct path in the cave

        treasure_room()
        
    input("Press Enter to exit...")