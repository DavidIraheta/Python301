# Add an API call to your CLI game that assigns a name to your player.


import random
import json
import os
import requests

name_length = 0
while not (name_length >= 2 and name_length <= 8):
    
        original_name = input("Enter your name: ")
        name_length = len(original_name)

URL = f"https://uzby.com/api.php?min={name_length}&max={name_length}"
response = requests.get(URL)
name = response.text

print(f"Welcome to the dungeon! In this world, your name won't be {original_name}.")
print(f"Instead, you'll be know as {name.upper()}!")



set_of_choices = {"left", "right", "far left", "far right"}
items = {"sword": 5, "golden axe": 10, "shield": 3, "potion": 15, "rusty dagger": 2}

# Player stats
player = {"name": "", "attack": random.randint(4, 8), "defense": 2, "health": 10, "inventory": []}

# Function to save the game
def save_game(player):
    if os.path.exists("save_file.json"):
        with open("save_file.json", "w") as save_file:
            json.dump(player, save_file)
        print("Game saved successfully!")
    else:
        print("Failed to save game. File does not exist.")

# Function to load the game
def load_game():
    if os.path.exists("save_file.json"):
        with open("save_file.json", "r") as save_file:
            return json.load(save_file)
    else:
        print("No save file found. Starting a new game.")
        return None
    
# Function to handle battles
def battle(player, enemy_name, enemy_attack, enemy_health):
    print(f"A {enemy_name} appears! Get ready to fight.")
    while player["health"] > 0 and enemy_health > 0:
        action = input("Do you want to 'attack', 'use' an item, or 'save' the game? ").lower().strip()
        
        if action == "save":
            save_game(player)
            continue
        
        if action == "use":
            print("Inventory:", player["inventory"])
            item_choice = input("Choose an item to use: ").lower().strip()
            
            if item_choice == "potion" and "potion" in player["inventory"]:
                player["health"] += items["potion"]
                player["inventory"].remove("potion")
                print(f"You used a potion. Current health: {player['health']}")
            elif item_choice in items and item_choice in player["inventory"]:
                print(f"You use the {item_choice} to temporarily boost your attack!")
                attack_power = player["attack"] + items[item_choice]
            else:
                print("Invalid choice or item not in inventory.")
                attack_power = player["attack"]
        else:
            attack_power = player["attack"]
        
        # Calculate attack damage
        attack_multiplier = random.uniform(0.8, 1.2)
        damage = int(attack_power * attack_multiplier)
        enemy_health -= damage
        print(f"You attack the {enemy_name}! It now has {max(0, enemy_health)} health.")
        
        if enemy_health <= 0:
            print(f"You defeated the {enemy_name}!")
            if enemy_name == "ogre":
                print("You found a potion!")
                player["inventory"].append("potion")
            return
        
        # Enemy attacks
        player["health"] -= enemy_attack
        print(f"The {enemy_name} attacks you! You now have {max(0, player['health'])} health.")
        
        if player["health"] <= 0:
            print("You have been defeated. Game over.")
            break

# Main game loop
def main():
    global player
    saved_player = load_game()
    if saved_player:
        player = saved_player
    else:
        player["name"] = input("To get started, please enter your name: ")
        print(f"Hello {player['name']}! Welcome to Echoes of the Keep!")
    
    while player["health"] > 0:
        door_choice = input("There are 4 doors in front of you. Choose one: left, right, far left, far right: ").lower().strip()
        
        if door_choice not in set_of_choices:
            print("Invalid choice. Try again.")
            continue
        
        if door_choice == "left":
            print("You have entered an empty room.")
            if input("Would you like to look around? yes / no: ").lower() == "yes":
                print("You found a sword!")
                if input("Take the sword? yes / no: ").lower() == "yes":
                    player["inventory"].append("sword")
                    print("You now have a sword! (Attack Power: 5)")
            print("You return to the castle lobby.")
        
        elif door_choice == "far left":
            battle(player, "ogre", enemy_attack=random.randint(3, 8), enemy_health=6)
        
        elif door_choice == "far right":
            print("You enter a room with two armoires.")
            if input("Open the large armoire? yes / no: ").lower() == "yes":
                print("You found a rusty dagger!")
                if input("Take the rusty dagger? yes / no: ").lower().strip() == "yes":
                    player["inventory"].append("rusty dagger")
                    print("You now have a rusty dagger! (Attack Power: 2)")
            
            if input("Open the small armoire? yes / no: ").lower() == "yes":
                battle(player, "goblin", enemy_attack=random.randint(1, 3), enemy_health=2)
        
        elif door_choice == "right":
            print("You encounter a dragon!")
            if input("Fight the dragon? yes / no: ").lower().strip() == "yes":
                if "golden axe" in player["inventory"]:
                    print("You bravely fight the dragon with your golden axe!")
                    battle(player, "dragon", enemy_attack=random.randint(10, 12), enemy_health=10)
                else:
                    print("Without the golden axe, you stand no chance. Game over.")
                    break
        print("\nCurrent Inventory:")
        for item in player["inventory"]:
            print(f"- {item} (Effect: {items.get(item, 'Unknown')}")
    print("Thank you for playing!")

if __name__ == "__main__":
    main()