import pygame
import os
from settings import *

class Obstacle:
    def __init__(self, sp_image):
        self.original_image = sp_image
        self.image = pygame.transform.scale(self.original_image, (SPRITE_WIDTH, SPRITE_HEIGHT))
        self.height = 50
        self.width = 50
        self.rect = self.image.get_rect()
        self.rect.width = SPRITE_WIDTH - 10
        self.rect.height = SPRITE_HEIGHT - 10

    def draw(self, coord, screen):
        self.x = coord[0]
        self.y = coord[1]
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        screen.blit(self.image, (self.x, self.y))
        # For debugging
        pygame.draw.rect(screen, (255, 0, 0), self.rect, 2)  # Draw a red rectangle with a width of 2 pixels
        
    def detect_collision(self, parachute):
        if self.rect.colliderect(parachute.rect):
            return True
        return False