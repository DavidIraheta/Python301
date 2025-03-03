import pygame
import random

pygame.init()

# game constants
width, height = 400, 600
fps = 60
gravity = 0.5  
jump_strength = -10  
pipe_speed = 3  
pipe_width = 70
gap_space = 150  

BLUE = (135, 206, 250)
YELLOW = (255, 255, 0)
GREEN = (0, 200, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

#game window
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Floopy Bean")

# Clock
clock = pygame.time.Clock()

# Fonts
font = pygame.font.Font(None, 40)
game_over_font = pygame.font.Font(None, 30)


class Bird:
    def __init__(self):
        self.x = 100
        self.y = height // 2
        self.width = 30
        self.height = 30
        self.velocity = 0  

    def update(self):
        self.velocity += gravity  
        self.y += self.velocity  

    def jump(self):
        self.velocity = jump_strength

    def draw(self, screen):
        pygame.draw.rect(screen, YELLOW, (self.x, self.y, self.width, self.height))

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)


class Pipe:
    def __init__(self, x):
        self.x = x
        self.gap_y = random.randint(100, height - 200)  
        self.passed = False  

    def update(self):
        self.x -= pipe_speed  

    def draw(self, screen):
        pygame.draw.rect(screen, GREEN, (self.x, 0, pipe_speed, self.gap_y))
        pygame.draw.rect(screen, GREEN, (self.x, self.gap_y + gap_space, pipe_width, height))

    def get_rects(self):
        top_rect = pygame.Rect(self.x, 0, pipe_width, self.gap_y)
        bottom_rect = pygame.Rect(self.x, self.gap_y + gap_space, pipe_width, height)
        return top_rect, bottom_rect


def game_over_screen(score):
    """Displays the Game Over screen and waits for restart."""
    screen.fill(BLUE)
    text = game_over_font.render("You didn't make it to Candy Mountain", True, RED)
    score_text = font.render(f"Score: {score}", True, WHITE)
    restart_text = font.render("Press SPACE to Restart", True, WHITE)

    screen.blit(text, (width // 2 - text.get_width() // 2, height // 3))
    screen.blit(score_text, (width // 2 - score_text.get_width() // 2, height // 2))
    screen.blit(restart_text, (width // 2 - restart_text.get_width() // 2, height // 1.5))

    pygame.display.flip()

    # Wait for SPACE key to restart
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                waiting = False  # Restart game


def main():
    """Main game loop."""
    bird = Bird()
    pipes = [Pipe(width + i * 200) for i in range(3)]  
    score = 0  
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird.jump()

        bird.update()
        for pipe in pipes:
            pipe.update()

            if not pipe.passed and pipe.x + pipe_width < bird.x:
                pipe.passed = True
                score += 1  

        if pipes[0].x + pipe_width < 0:
            pipes.pop(0)  
            pipes.append(Pipe(width))  

        # Collision detection
        bird_rect = bird.get_rect()
        for pipe in pipes:
            top_rect, bottom_rect = pipe.get_rects()
            if bird_rect.colliderect(top_rect) or bird_rect.colliderect(bottom_rect):  
                running = False  

        if bird.y + bird.height > height:
            running = False  

        screen.fill(BLUE)  
        bird.draw(screen)
        for pipe in pipes:
            pipe.draw(screen)

        score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))

        pygame.display.flip()
        clock.tick(fps)

    # Show game over screen and restart
    game_over_screen(score)
    main()  


# Start the game
main()
