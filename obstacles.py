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

    def draw(self, coord, screen):
        self.x = coord[0]
        self.y = coord[1]
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        screen.blit(self.image, (self.x, self.y))
        # pygame.draw.rect(screen, self.sp_image, self.rect)
        
    def detect_collision(self, parachute):
        if self.rect.colliderect(parachute.rect):
            return True
        return False