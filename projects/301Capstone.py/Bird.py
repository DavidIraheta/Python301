#create a gae similiar to flappy bird 
import arcade
import random 
import os 
import math 

# Basic arcade shooter

# Imports
import arcade
import random

#constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Floopy Bird"
SCALING = 2.0
GRAVITY = 0.5
FLAP_STRENGTH = 10
PIPE_WIDTH = 100
PIPE_HEIGHT = 500

# Player class
class Bird(arcade.Sprite):
    def __init__(self):
        super().__init__("images/bird.png", SCALING)
        self.center_x = 100
        self.center_y = SCREEN_HEIGHT // 2
        self.velocity = 0

    def update(self):
        self.velocity -= GRAVITY
        self.center_y += self.velocity

    def flap(self):
        self.velocity = FLAP_STRENGTH

# Pipe class
class Pipe(arcade.Sprite):
    def __init__(self, x, y, flipped):
        super().__init__("images/pipe.png", SCALING)
        self.center_x = x
        self.center_y = y
        self.angle = 180 if flipped else 0

    def update(self):
        self.center_x -= 5

# Game class
class FloopyBird(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.SKY_BLUE)

        self.bird = Bird()
        self.pipes = []
        self.score = 0
        self.game_over = False
        self.pipe_timer = 0

    def on_draw(self):
        arcade.start_render()

        self.bird.draw()
        for pipe in self.pipes:
            pipe.draw()

        arcade.draw_text(f"Score: {self.score}", 10, SCREEN_HEIGHT - 20, arcade.color.BLACK, 16)

        if self.game_over:
            arcade.draw_text("Game Over", SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2, arcade.color.BLACK, 20)

    def update(self, delta_time):
        if not self.game_over:
            self.bird.update()

            for pipe in self.pipes:
                pipe.update()
                if pipe.center_x < -PIPE_WIDTH:
                    self.pipes.remove(pipe)
                    self.score += 1

            self.pipe_timer += 1
            if self.pipe_timer == 120:
                self.pipe_timer = 0
                y = random.randint(PIPE_HEIGHT, SCREEN_HEIGHT - PIPE_HEIGHT)
                self.pipes.append(Pipe(SCREEN_WIDTH + PIPE_WIDTH // 2, y + PIPE_HEIGHT // 2, False))
                self.pipes.append(Pipe(SCREEN_WIDTH + PIPE_WIDTH // 2, y - PIPE_HEIGHT // 2, True))

            if self.bird.center_y < 0 or self.bird.center_y > SCREEN_HEIGHT:
                self.game_over = True

            for pipe in self.pipes:
                if arcade.check_for_collision(self.bird, pipe):
                    self.game_over = True

    def on_key_press(self, key, modifiers):
        if key == arcade.key.SPACE:
            self.bird.flap()

# Main game
if __name__ == "__main__":
    window = FloopyBird()
    arcade.run()