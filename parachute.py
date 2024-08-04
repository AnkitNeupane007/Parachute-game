import pygame
import os
from settings import *

class Parachute:
    def __init__(self, speed, x, y, left_key, right_key, parachute_image):
        self.original_image = parachute_image
        self.image = pygame.transform.scale(self.original_image, (PARACHUTE_WIDTH, PARACHUTE_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rect.width = PARACHUTE_WIDTH - 13
        self.rect.height = PARACHUTE_HEIGHT -10
        self.speed = speed
        self.left_key = left_key
        self.right_key = right_key

    def update(self):
        self.rect.y += self.speed
        
        keys = pygame.key.get_pressed()
        if keys[self.left_key] and self.rect.x > 0:
            self.rect.x -= PARACHUTE_HORIZONTAL_SPEED
        if keys[self.right_key] and self.rect.x < SCREEN_WIDTH - self.rect.width:
            self.rect.x += PARACHUTE_HORIZONTAL_SPEED

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x-7, self.rect.y - 4))  # Draw the parachute image
        # For debugging
        pygame.draw.rect(screen, (255, 0, 0), self.rect, 2)  # Draw a red rectangle with a width of 2 pixels

        
    def detect_out_of_bounds(self):
        if (self.rect.y > SCREEN_HEIGHT - self.rect.height):
            return True
        return False
    
    def wind(self, wind_speed, wind_direction):
        if wind_direction ==  'left':
            if self.rect.x > 0:
                self.rect.x -= wind_speed
        elif wind_direction == 'right':
            if self.rect.x < SCREEN_WIDTH - self.rect.width:
                self.rect.x += wind_speed