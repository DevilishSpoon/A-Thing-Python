#Imports
import random

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
    print(f"/"*10)
    print()
    print("Items in your inventory!")
    for item in inventory:
        print(f"-{item}")
    print()
    print(f"/"*10)

def main_menu():
    print(f"/"*10)
    print("Hero's Journey")
    print()
    choice_game = input(" Adventure?\n Check Inventory?\n Shop?\nWhat would you like to do?").lower()

def fight():


#Welcome
print("Welcome to Hero's journey!")
print("There are adventures, shops, and more in this game!")
print("first pick a starting weapon!")
for item in weapons:
    if item == "broken sword":
        break
    print(item)


chosen_weapon = input(f"What weapon would you like to use?\n").lower()
while selected_weapon == "":
    if chosen_weapon == "sword" or chosen_weapon == "katana":
        inventory.append(f"{chosen_weapon}")
        selected_weapon = chosen_weapon
main_menu()
