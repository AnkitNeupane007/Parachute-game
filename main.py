import pygame
import os
import sys
from settings import *
from level import start_level_1, start_level_2, start_level_3

def home_screen(clock):
    button_width = SCREEN_WIDTH * 0.15625  # Example: 125 / 800
    button_height = SCREEN_HEIGHT * 0.0833  # Example: 50 / 600
    button_y = SCREEN_HEIGHT * 0.8333  # Example: 500 / 600

    buttons = [
        Button("Level 1", SCREEN_WIDTH * 0.1375, button_y, button_width, button_height, ORANGE, lambda: start_level_1(clock, home_screen)),
        Button("Level 2", SCREEN_WIDTH * 0.41875, button_y, button_width, button_height, ORANGE, lambda: start_level_2(clock, home_screen)),
        Button("Level 3", SCREEN_WIDTH * 0.7, button_y, button_width, button_height, ORANGE, lambda: start_level_3(clock, home_screen)),
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
