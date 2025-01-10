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

class Pokemon:
    def __init__(self, name, primary_type, max_hp, hp):
        self.name = name
        self.primary_type = primary_type
        self.max_hp = max_hp
        self.hp = hp

    def __str__(self):
        return f"{self.name} ({self.primary_type}): has {self.hp/self.max_hp} HP left."
    def feed(self):
        self.hp += 10
        if self.hp > self.max_hp:
            self.hp = self.max_hp
        print(f"{self.name} was fed and now has {self.hp} HP.")
#make them battle and decide a winner
    def battle(self, other):
        print(f"{self.name} battles {other.name}")
    