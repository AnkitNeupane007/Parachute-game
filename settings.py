import pygame
import os

# Initialize Pygame
pygame.init()

# Fonts
font = pygame.font.Font(None, 36)

# Home screen image
home_screen_image = pygame.image.load(os.path.join('objects/home/', 'home_screen.png'))
home_screen_image = pygame.transform.scale(home_screen_image, (800, 600))

# Level background image
level_background = pygame.image.load(os.path.join('objects/home', 'level.png'))
level_background = pygame.transform.scale(level_background, (800, 600))

# Sprite scale
SPRITE_HEIGHT = 50
SPRITE_WIDTH = 50

# Sprite images
skull1_sp = pygame.image.load(os.path.join('objects/obstacles', 'Skull1.png'))
building_sp = pygame.image.load(os.path.join('objects/obstacles', 'Building.png'))
skull2_sp = pygame.image.load(os.path.join('objects/obstacles', 'Skull2.png'))
bomb_sp = pygame.image.load(os.path.join('objects/obstacles', 'Bomb.png'))
xmas_sp = pygame.image.load(os.path.join('objects/obstacles', 'Xmas.png'))

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("2D Parachute Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (165, 237, 140)
RED = (249, 110, 110)
YELLOW = (255, 255, 0)
PURPLE = (128, 0, 128)
BLUE = (0, 0, 255)
GRAY = (128, 128, 128)
ORANGE =(237, 176, 70)
LIGHT_WHITE = (240, 240, 240)

# Parachute settings
PARACHUTE_WIDTH = 50
PARACHUTE_HEIGHT = 50
PARACHUTE_HORIZONTAL_SPEED = 5

# Wind settings
wind_direction = ('left', 'right')

# Parachutes available
PARACHUTE_1 = pygame.image.load(os.path.join('objects/parachute/pngs', 'white.png'))
PARACHUTE_2 = pygame.image.load(os.path.join('objects/parachute/pngs', 'army_green.png'))
PARACHUTE_3 = pygame.image.load(os.path.join('objects/parachute/pngs', 'army_canvas.png'))

PARACHUTE_4 = pygame.image.load(os.path.join('objects/parachute/pngs', 'purple_yellow.png'))
PARACHUTE_5 = pygame.image.load(os.path.join('objects/parachute/pngs', 'multicolor.png'))

class Button:
    def __init__(self, text, x, y, width, height, color, callback, image=None):
        self.text = text
        self.rect = pygame.Rect(x, y, width, height)
        self.callback = callback
        self.color = color
        self.image = image
        if image:
            self.image = pygame.transform.scale(image, (60, 60))
            self.image_rect = self.image.get_rect()
            self.image_rect.topleft = (x + width/8, y + height/8) #(x + self.rect.width + 10, y + 7)
        
    def display(self, screen):  # For image
        pygame.draw.rect(screen, self.color, self.rect)
        screen.blit(self.image, self.image_rect)

    def draw(self, screen): # For text
        pygame.draw.rect(screen, self.color, self.rect)
        text_surf = font.render(self.text, True, LIGHT_WHITE)
        screen.blit(text_surf, (self.rect.x + self.rect.width/6, self.rect.y + self.rect.height/4))


    def check_click(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos):
            self.callback()