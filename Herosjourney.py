#Imports
import random

#Game start
inventory = ()
max_health = 10

items = ()
weapons = {
"sword": {"damage": 8, "durability": 10},
"katana": {"damage": 12, "durability": 10}
}


for item in weapons:
    print(item)
selected_weapon = input(f"What weapon would you like to use?\n")
print(weapons[selected_weapon]["damage"])
