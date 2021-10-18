#Imports
import random

#Game start
inventory = []
max_health = 10
selected_weapon = ""

items = {}
weapons = {
"sword": {"damage": ["durability"]*2, "durability": 10},
"katana": {"damage": 12, "durability": 10},
"broken sword": {"damage": 100, "durability": 1},
"halberd": {"damage": ["durability"]*2, "durability": 10}
}

#Functions
def checkinv():
    for item in inventory:
        print(item)

#Welcome
print("Welcome to Hero's journey!")
print("There are adventures, shops, and more in this game!")
print("first pick a starting weapon!")
for item in weapons:
    if item == "katana":
        break
    print(item)


chosen_weapon = input(f"What weapon would you like to use?\n").lower()
while selected_weapon == "":
    if chosen_weapon == "sword" or chosen_weapon == "katana":
        inventory.append(f"{chosen_weapon}")
        selected_weapon = chosen_weapon
print(inventory)
checkinv()
