import random 
import time 
from Characters import Hero, Opponent


def main():
    print_welcome()
    play_game()

def print_welcome():
    print("""-----------------------------------------------------
          ------------Welcome to Waluigi's Castle!-------------
          ------------------------------------------------------
    Using his dark magic, Bowser trapped Mario, Luigi, and Princess Peach in a crystal labyrinth,
    leaving the kingdom vulnerable to his chaotic rule.
    The toads cried for a savior, but no one dared to step up.
    No one, except Waluigi.
    Your friends need to to restore peace to the mushroom kingdom.
    You must defeat Bowser and his minions to save them.""")

def play_game():
    Opponents = [
    Opponent("Goomba", 1), 
    Opponent("Koopa", 2),
    Opponent("Boo", 4), 
    Opponent("Wiggler", 6),
    Opponent("Thwomp", 8),
    Opponent("Dry Bones", 10),
    Opponent("Shy Guy", 12),
    Opponent("Chain Chomp", 18),
    Opponent("Bowser", 45)
    ]
    hero = Hero("Waluigi", 1, 100)

    while True:
        current_opponent = random.choice(Opponents)
        print(f"Watch out Waliuigi! a" {current_opponent.name} \
              at Level {current_opponent.level} has appeared.\n")