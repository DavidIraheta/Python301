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
    Your friends need you to restore peace to the mushroom kingdom.
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
        print(f"Watch out Waliuigi! a {current_opponent.name} \
              at Level {current_opponent.level} has appeared.\n")
    
        cmd = input("Do you want to [a]ttack , [r]unaway , or [l]ook around? ").strip().lower()
        while cmd not in ["a", "r", "l", "q"]:
          print("Please enter one of the letters[a],[r], or [l] to play").strip().lower()
          print("To exit the game type [q] to quit")
          cmd = input("Do you want to [a]ttack , [r]unaway , or [l]ook around? ").strip().lower()
        
        if cmd == "a":
            if hero.attack(current_opponent):
                Opponents.remove(current_opponent)
            else:
                hero.take_damage(current_opponent.attack(hero))
                time.sleep(2)
                print(f"{hero.name} decided to take a nap for a moment, he regains some health.")
        
        elif cmd == "r":
            print(f"{hero.name} ran away from the {current_opponent.name}!")

        elif cmd == "l":
            print(f"{hero.name} whacks his tennis racket around at nothing around and sees:")
            for opponent in Opponents:
                print(f"* A {opponent.name} at Level {opponent.level}")
        
        elif cmd == "q":
            print("\n You left all your friends hangning in danger and ran away")
            break


if __name__ == "__main__":
    main()

