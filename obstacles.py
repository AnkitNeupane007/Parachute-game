import pygame
import os

class Obstacle:
    def __init__(self, color):
        # self.original_image = pygame.image.load(os.path.join('objects/obstacles', 'Xmas.png'))
        # self.image = pygame.transform.scale(self.original_image, (50, 50))
        # self.rect = self.image.get_rect()
        self.width = 50
        self.height = 50
        self.color = color

    def draw(self, coord, screen):
        self.x = coord[0]
        self.y = coord[1]
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        # screen.blit(self.image, (self.x, self.y))
        pygame.draw.rect(screen, self.color, self.rect)