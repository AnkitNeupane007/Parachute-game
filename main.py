import pygame
import os
import sys
from settings import *
from level import start_level_1, start_level_2, start_level_3

def home_screen(clock):
    buttons = [
        Button("Level 1", 110, 500, 125, 50, ORANGE, lambda: start_level_1(clock, home_screen)),
        Button("Level 2", 335, 500, 125, 50, ORANGE, lambda: start_level_2(clock, home_screen)),
        Button("Level 3", 560, 500, 125, 50, ORANGE, lambda: start_level_3(clock, home_screen)),
    ]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            for button in buttons:
                button.check_click(event)

        screen.fill(WHITE)
        screen.blit(home_screen_image, home_screen_image.get_rect())

        for button in buttons:
            button.draw(screen)
        pygame.display.flip()

        clock.tick(60)

if __name__ == "__main__":
    clock = pygame.time.Clock()
    home_screen(clock)
