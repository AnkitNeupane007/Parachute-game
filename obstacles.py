import pygame

class Obstacle:
    def __init__(self, color):
        self.width = 50
        self.height = 50
        self.color = color

    def draw(self, coord, screen):
        self.x = coord[0]
        self.y = coord[1]
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(screen, self.color, self.rect)