#build a card game using classes and inheritance

import arcade
import random

# Constants
WIDTH, HEIGHT = 800, 600
CARD_WIDTH, CARD_HEIGHT = 80, 120
COLORS = ["red", "green", "blue", "yellow"]
VALUES = list(range(1, 10)) + ["skip", "reverse", "+2"]

# Card base class
class Card:
    def __init__(self, color, value):
        self.color = color
        self.value = value

    def draw(self, x, y):
        arcade.draw_rect_filled(x, y, CARD_WIDTH, CARD_HEIGHT, arcade.color.WHITE)
        arcade.draw_text(f"{self.color} {self.value}", x - 20, y - 10, arcade.color.BLACK, 12)

# Deck class
class Deck:
    def __init__(self):
        self.cards = [Card(color, value) for color in COLORS for value in VALUES] * 2
        random.shuffle(self.cards)

    def draw_card(self):
        return self.cards.pop() if self.cards else None

# Player class
class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw(self, deck, num=1):
        for _ in range(num):
            card = deck.draw_card()
            if card:
                self.hand.append(card)

# Game class using Arcade API
class UnoGame(arcade.Window):
    def __init__(self):
        super().__init__(WIDTH, HEIGHT, "UNO Game")
        self.deck = Deck()
        self.player = Player("Player 1")
        self.player.draw(self.deck, 7)

    def on_draw(self):
        arcade.start_render()
        for i, card in enumerate(self.player.hand):
            card.draw(50 + i * (CARD_WIDTH + 10), HEIGHT - 150)

    def on_key_press(self, key, modifiers):
        if key == arcade.key.Q:
            arcade.close_window()

if __name__ == "__main__":
    game = UnoGame()
    arcade.run()
