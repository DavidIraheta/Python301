# Build a very basic Pokémon class that allows you to simulate battles
# in a Rock-Paper-Scissors game mechanic, as well as feed your Pokémon.
#
# The class should follow these specifications:
#
# - Each Pokemon should have a `name`, `primary_type`, `max_hp` and `hp`
# - Primary types should be limited to `water`, `fire` and `grass`
# - Implement a `battle()` method based on rock-paper-scissors that
#   decides who wins based only on the `primary_type`:
#       water > fire > grass > water
# - Display messages that explain who won or lost a battle
# - If a Pokemon loses a battle, they lose some of their `hp`
# - If you call the `feed()` method on a Pokemon, they regain some `hp`
# - Implement a `__str__()` method that displays the Pokemon's attributes
# - Implement a `pokemon_type_result()` method that determines the result
#   of a battle based on the primary types of two Pokemon


class Pokemon:
    def __init__(self, name, primary_type, hp, max_hp):
        self.name = name
        self.primary_type = primary_type
        self.max_hp = max_hp
        self.hp = hp

    def __str__(self):
        return f"{self.name} ({self.primary_type}): has {self.hp}/{self.max_hp} HP left."

    def feed(self):
        self.hp += 10
        if self.hp > self.max_hp:
            self.hp = self.max_hp
        print(f"{self.name} had a snack and now has {self.max_hp} HP.")

    def battle(self, other):
        print(f"{self.name} battles {other.name}")

        # Determine the result of the battle
        result = self.pokemon_type_result(self.primary_type, other.primary_type)

        if result == "win":
            print(f"{self.name} won the battle against {other.name}!")
            other.hp -= 20
            if other.hp < 0:
                other.hp = 0
        elif result == "lose":
            print(f"{self.name} lost the battle against {other.name}.")
            self.hp -= 20
            if self.hp < 0:
                self.hp = 0
        else:
            print(f"The battle between {self.name} and {other.name} ended in a tie.")

    @staticmethod
    def pokemon_type_result(type1, type2):
        # Map types to indices
        type_map = {"water": 0, "fire": 1, "grass": 2}
        
        # Validate types
        if type1 not in type_map or type2 not in type_map:
            raise ValueError("Invalid Pokemon type. Types must be 'water', 'fire', or 'grass'.")

        # Define win-loss matrix
        wl_matrix = [
            [0, 1, -1],  # water
            [-1, 0, 1],  # fire
            [1, -1, 0]   # grass
        ]

        # Get the result from the matrix
        result_index = wl_matrix[type_map[type1]][type_map[type2]]
        result_map = {0: "tie", 1: "win", -1: "lose"}
        return result_map[result_index]

if __name__ == '__main__':
    b = Pokemon("Bulbasaur", "grass", 40, 100)
    c = Pokemon("Charmander", "fire", 50, 100)

    print(b)
    print(c)

    b.battle(c)
    c.battle(b)

    # b.feed()
    # c.feed()

    # print(b)
    # print(c)
