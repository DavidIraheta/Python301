# build a card game using classes and inheritance

import arcade
import random

# Constants
WIDTH, HEIGHT = 800, 600
CARD_WIDTH, CARD_HEIGHT = 80, 120
SCREEN_TITLE = "Welcome to UNOS"
COLORS = ["red", "green", "blue", "yellow"]
VALUES = list(range(2, 9)) + ["skip", "reverse", "+2"]

# Card base class
class Card:
    def __init__(self, color, value):
        self.color = color
        self.value = value

    def draw(self, x, y):
        # Draw card background
        arcade.draw_rectangle_filled(x, y, CARD_WIDTH, CARD_HEIGHT, arcade.color.YELLOW)

        # Draw card border
        arcade.draw_rectangle_outline(x, y, CARD_WIDTH, CARD_HEIGHT, arcade.color.BLACK, 2)

        # Draw card text (centered)
        text = f"{self.color} {self.value}"
        arcade.draw_text(text, x - CARD_WIDTH // 2 + 5, y - 10, arcade.color.BLACK, 12)

# Deck class
class Deck:
    def __init__(self):
        # Create a deck of UNO cards (2 copies of each)
        self.cards = [Card(color, value) for color in COLORS for value in VALUES] * 2
        random.shuffle(self.cards)

    def draw_card(self):
        # Draw a card from the deck (if available)
        return self.cards.pop() if self.cards else None

# Player class
class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw(self, deck, num=1):
        # Draw a specified number of cards from the deck
        for _ in range(num):
            card = deck.draw_card()
            if card:
                self.hand.append(card)

# Game class using Arcade API
class UnoGame(arcade.Window):
    def __init__(self):
        super().__init__(WIDTH, HEIGHT, "UNO Game")

        # Set the background color
        super().__init__(WIDTH, HEIGHT, "UNO Game", resizable=True)
        arcade.set_background_color(arcade.color.WHITE)

        # Initialize deck and player
        self.deck = Deck()
        self.player = Player("Player 1")
        self.player.draw(self.deck, 7)  # Draw 7 cards to start

    arcade.start_render

    def on_draw(self):
        self.clear()

        # Display player hand (spacing to prevent overlap)
        for i, card in enumerate(self.player.hand):
            x_position = 50 + i * (CARD_WIDTH + 20)  # Increased spacing to avoid overlap
            card.draw(x_position, HEIGHT - 150)

        # Draw instruction text
        arcade.draw_text("Press 'Q' to quit", 10, 10, arcade.color.GREEN, 14)

        arcade.finish_render

    def on_key_press(self, key, modifiers):
        if key == arcade.key.Q:
            arcade.close_window()

    

if __name__ == "__main__":
    game = UnoGame()
    arcade.run()


