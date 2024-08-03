import pygame
import os

# Initialize Pygame
pygame.init()

# Fonts
font = pygame.font.Font(None, 36)

# Home screen image
home_screen_image = pygame.image.load(os.path.join('objects/home/', 'home_screen.jpeg'))
home_screen_image = pygame.transform.scale(home_screen_image, (800, 600))

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("2D Parachute Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Parachute settings
PARACHUTE_WIDTH = 50
PARACHUTE_HEIGHT = 50
PARACHUTE_HORIZONTAL_SPEED = 5

class Button:
    def __init__(self, text, x, y, color, callback):
        self.text = text
        self.rect = pygame.Rect(x, y, 200, 50)
        self.callback = callback
        self.color = color

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        text_surf = font.render(self.text, True, BLACK)
        screen.blit(text_surf, (self.rect.x + 20, self.rect.y + 10))

    def check_click(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos):
            self.callback()