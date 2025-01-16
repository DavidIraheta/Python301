# use OOP techniques to create a text-based command-line interface role-playing game.
#Build a text-based role-playing game that has at least two classes:
#Hero(): the protagonist of your game that the player controls and identifies with. There should be only one hero.
#Opponent(): the challengers that the player meets throughout the gameplay. There should be multiple opponents.
#The hero should encounter multiple opponents of different strengths or levels. They should be able to perform different actions when meeting an opponent.
# These actions should be at a minimum: attack or run away
#If the Hero chooses to attack, the program decides through a simulated dice throw that takes the current level into account whether the hero or the opponent wins this round:
#Also, implement consequences for winning and losing, e.g., forcing the hero to wait a few seconds before continuing the game in case they lose. 
# Or removing the opponent from the opponent pool in case the hero wins.
# You'll have to implement both attributes and methods for both of your classes. Think about what you'll need so you can model the described functionality

import random
import time

class Hero:
    def __init__(self, name, level = 1, health = 100):
        self.name = name
        self.level = level
        self.health = health


    def attack(self, opponent):
        print(f"You {self.name} attacks {opponent.name}!")
       
        Hero_roll = random.randint(1, 12) * self.level
        Opponent_roll = random.randint(1, 12) * opponent.level

        print(f"You roll {Hero_roll}...")
        print(f"{opponent.name} rolls {Opponent_roll}...")

        if Hero_roll >= Opponent_roll:
            print(f"{self.name} has defeated {opponent.name}!")
            return True
        else:
            print(f"{self.name} has been defeated by {opponent.name}!")
            return False
        
    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            print(f"{self.name} has died!")
            exit()

    def heal(self, heal):
        self.health += heal

class Opponent:
    def __init__(self, name, level = 1):
        self.name = name
        self.level = level
        self.health = level * 20
    def attack (self, hero):
        return random.randint(1, 6) + self.level 
    
    def take_damage(self, damage):
        self.health -= damage
        
    def __repr__(self):
        return f"Oppononent: {self.name} at Level {self.level}"
