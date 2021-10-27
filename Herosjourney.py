#Imports
import random
import time
from os import system, name

#Game start
inventory = ["health potion"]
max_health = 10
p_health = 10
selected_weapon = ""
gold = 0
level = 1
heals_used = 0
times_play = 0
choice_game = ""

#Defining weapons and items
items = {
"health potion": {"heal": 5},
"big health potion": {"heal": 10},
"heart container": {"max health increase": 1},
"repair powder": {"weapon durability heal": 1},
"forge weapon": {"weapon max durability increase": 1}
}
weapons = {
"sword": {"damage": 2, "durability": 10},
"katana": {"damage": 4, "durability": 5},
"broken sword": {"damage": 100, "durability": 1},
"halberd": {"damage": 3, "durability": 15}
}

#Enemies

enemies = {
"Ogre": {"damage": 3, "health": 5},
"Goblin": {"damage": 1, "health": 3},
"Poop": {"damage": 0, "health": 1},
"Honey bee": {"damage": 2, "health": 3}
}
npcs = {
"Shopkeeper"
}
en_name = ""
#Functions
def checkinv():
    #Clear screen
    if name == "nt":
        _ = system("cls")
    else:
        _ = system("clear")
    print(f"/"*10)
    print(f"Health: {p_health}/{max_health}\n")
    print("Items in your inventory!")
    for item in inventory:
        if item in weapons:
            print(f" - {item}, {weapons[item]}")
        elif item in items:
            print(f" - {item}, {items[item]}")
    print(f"Gold: {gold}")
    print()
    print(f"/"*10)

def main_menu():
    global times_play
    global choice_game
    #Clear screen
    if name == "nt":
        _ = system("cls")
    else:
        _ = system("clear")
    print(f"/"*10)
    print()
    print("Hero's Journey")
    print("--------------")
    choice_game = input(" Colosseum?\n Adventure?\n Check Inventory?\n Shop?\n Quit?\nWhat would you like to do?\n").lower()
    match choice_game:
        case "colosseum":
            times_play = int(input("How many times would you like to fight? "))
            fight()
            main_menu()
        case "check inventory":
            checkinv()
            input("press enter to continue...")
            main_menu()
        case "shop":
            print("Shop's closed sorry :(")
            input("press enter to continue...")
            main_menu()
        case "quit":
            super_sure = input("Are you sure you would like to quit? yes or no?\n").lower()
            if super_sure == "yes" or "y":
                quit("Goodbye!")
            else:
                main_menu()
        case "adventure":
            adventure()
            main_menu()
        case _:
            main_menu()

def fight():
    #unpack values
    global p_health
    global heals_used
    global gold
    global en_name
    global times_play
    global p_wepdurab
    if not en_name:
        en_name = random.choice(list(enemies.keys()))
    en_damage,en_health = enemies[en_name].values()

    #encounter
    print(f"\nFound an {en_name}! Health: {en_health} Damage: {en_damage}")
    en_reward = en_health
    while en_health > 0:
        time.sleep(1)

        #attack
        if p_wepdurab > 0:
            dam_dealt = random.randrange(p_damage-1, int(p_damage*1.5)+1)
            match dam_dealt:
                case dam_dealt if dam_dealt > p_damage:
                    print(f"Critical hit! Dealt {dam_dealt} damage!")
                case dam_dealt if dam_dealt == p_damage:
                    print(f"Hit! Dealt {dam_dealt} damage!")
                    p_wepdurab -= 1
                case dam_dealt if dam_dealt < p_damage:
                    print(f"Weak hit! Dealt {dam_dealt} damage!")
                    p_wepdurab -= 1
            en_health -= dam_dealt
            print(f"{en_name}, Health: {en_health} Damage: {en_damage}\n")
            time.sleep(1)
        else:
            dam_dealt = random.randrange(1-1, int(1*1.5)+1)
            match dam_dealt:
                case dam_dealt if dam_dealt > 1:
                    print(f"Critical hit! Dealt {dam_dealt} damage!")
                case dam_dealt if dam_dealt == 1:
                    print(f"Hit! Dealt {dam_dealt} damage!")
                    p_wepdurab -= 1
                case dam_dealt if dam_dealt < 1:
                    print(f"Weak hit! Dealt {dam_dealt} damage!")
                    p_wepdurab -= 1
            en_health -= dam_dealt
            print(f"{en_name}, Health: {en_health} Damage: {en_damage}\n")
            time.sleep(1)
        #Taking damage
        en_dam_dealt = random.randrange(en_damage-1, int(en_damage*1.5)+1)
        if en_health > 0:
            if en_dam_dealt < 0:
                en_dam_dealt = 0
            match en_dam_dealt:
                case en_dam_dealt if en_dam_dealt > en_damage:
                    print(f"Critical hit! Took {en_dam_dealt} damage!")
                case en_dam_dealt if en_dam_dealt == en_damage:
                    print(f"Hit! Took {en_dam_dealt} damage!")
                case en_dam_dealt if en_dam_dealt < p_damage:
                    print(f"Weak hit! Took {en_dam_dealt} damage!")
            p_health -= en_dam_dealt
        print(f"You have {p_health} health left!\n")
        time.sleep(1)

        #weapon durability
        if p_wepdurab < 5 and "repair powder" not in inventory:
            print(f"Warning your weapon is going to break! durability is at {p_wepdurab}")
            time.sleep(1)

        #death
        if p_health <= 0:
            print("You Died. :(")
            input("press enter to quit")
            quit()

        #healing
        while p_health <= max_health-5 and "health potion" in inventory:
            use_heal()
            heals_used += 1
        if heals_used > 0:
            print(f"Healed {heals_used*5} and used {heals_used} potions!\n")
            heals_used = 0
            time.sleep(1)

    #fight gold system
    gold_gained = random.randrange(int(en_reward/2), int(en_reward*2))
    if choice_game == "colosseum":
        gold_gained += en_reward
    gold += gold_gained
    print(f"Gained {gold_gained} gold! Now you have {gold} gold!")
    en_name = ""

    #times play system
    if times_play <= 1:
        input("press enter to continue...")
    elif times_play > 1:
        times_play -=1
        fight()


def use_heal():
    global p_health
    if "health potion" in inventory:
        inventory.remove("health potion")
        p_health += 5

def adventure():
    print("hi")

def event():
    print("hi\n")
    input("press enter to continue...")

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
    print(f" - {item}")
    print(f"{weapons[item]}\n")

while selected_weapon == "":
    chosen_weapon = input(f"What weapon would you like to use?\n").lower()
    if chosen_weapon == "sword" or chosen_weapon == "katana":
        inventory.append(f"{chosen_weapon}")
        selected_weapon = chosen_weapon
        p_damage = weapons[selected_weapon]["damage"]
        p_wepdurab = weapons[selected_weapon]["durability"]
    elif chosen_weapon == "":
        quit()

main_menu()
