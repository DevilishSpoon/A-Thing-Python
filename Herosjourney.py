#Imports
import random
from os import system, name

#Game start
inventory = []
max_health = 10
selected_weapon = ""
gold = 100

#Defining weapons and items
items = {}
weapons = {
"sword": {"damage": 10, "durability": 12},
"katana": {"damage": 12, "durability": 10},
"broken sword": {"damage": 100, "durability": 1},
"halberd": {"damage": 15, "durability": 20}
}

#Enemies
enemies = ["Ogre","Goblin","Poop"]

#Functions
def checkinv():
    #Clear screen
    if name == "nt":
        _ = system("cls")
    else:
        _ = system("clear")
    print(f"/"*10)
    print()
    print("Items in your inventory!")
    for item in inventory:
        print(f"-{item}")
    print()
    print(f"/"*10)

def main_menu():
    #Clear screen
    if name == "nt":
        _ = system("cls")
    else:
        _ = system("clear")
    print(f"/"*10)
    print()
    print("Hero's Journey")
    print("--------------")
    choice_game = input(" Adventure?\n Check Inventory?\n Shop?\n Quit?\nWhat would you like to do?\n").lower()
    match choice_game:
        case "check inventory":
            checkinv()
            input("press any button to continue...")
            main_menu()
        case "shop":
            print("Shop's closed sorry :(")
            input("press any button to continue...")
            main_menu()
        case "quit":
            super_sure = input("Are you sure you would like to quit? yes or no?\n").lower()
            if super_sure == "yes":
                quit("Goodbye!")
            else:
                main_menu()
        case _:
            main_menu()
def fight():
    print("hi")

#Welcome
#Clear screen
if name == "nt":
    _ = system("cls")
else:
    _ = system("clear")
print("/"*10)
print()
print("Welcome to Hero's journey!")
print("There are adventures, shops, and more in this game!")
print("first pick a starting weapon!")
print()
for item in weapons:
    if item == "broken sword":
        break
    print(f"-{item}")
    print(f"{weapons[item]}\n")

while selected_weapon == "":
    chosen_weapon = input(f"What weapon would you like to use?\n").lower()
    if chosen_weapon == "sword" or chosen_weapon == "katana":
        inventory.append(f"{chosen_weapon}")
        selected_weapon = chosen_weapon
    elif chosen_weapon == "":
        quit()

main_menu()
