import pygame
import sys
from settings import *
from parachute import Parachute
from obstacles import *
from end import end_screen

def level_1(clock, home_screen_callback):
    parachute1 = Parachute(2, pygame.K_LEFT, pygame.K_RIGHT)
    parachute2 = Parachute(2, pygame.K_a, pygame.K_d)
    
    # Red: Tree
    # Blue: Rock
    # Yellow: Bird
    # Green: Building
    # Purple: Cloud

    obstacles = [Obstacle(RED),  
                 Obstacle(BLUE),                   
                 Obstacle(YELLOW),
                 Obstacle(GREEN),
                 Obstacle(PURPLE),
                 Obstacle(BLUE)]
    
    obstacles_coordinates = [(100, 300),
                             (480, 250),
                             (250, 350),
                             (450, 500),
                             (550, 100),
                             (650, 400)]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        parachute1.update()
        parachute2.update()

        if parachute1.detect_out_of_bounds() or parachute2.detect_out_of_bounds():
            end_screen(clock, home_screen_callback)

        screen.fill(WHITE)
        parachute1.draw(screen)
        parachute2.draw(screen)

        for obstacle, coord in zip(obstacles, obstacles_coordinates):
            obstacle.draw(coord, screen)
            

        pygame.display.flip()
        clock.tick(60)

def level_2(clock, home_screen_callback):
    parachute1 = Parachute(2, pygame.K_LEFT, pygame.K_RIGHT)
    parachute2 = Parachute(2, pygame.K_a, pygame.K_d)

    obstacles = [
        Obstacle(RED),    # Tree
        Obstacle(RED),    # Tree
        Obstacle(RED),    # Tree
        Obstacle(BLUE),   # Rock
        Obstacle(BLUE),   # Rock
        Obstacle(BLUE),   # Rock
        Obstacle(YELLOW), # Bird
        Obstacle(YELLOW), # Bird
        Obstacle(YELLOW), # Bird
        Obstacle(GREEN),  # Building
        Obstacle(GREEN),  # Building
        Obstacle(GREEN),  # Building
        Obstacle(PURPLE), # Cloud
        Obstacle(PURPLE), # Cloud
        Obstacle(PURPLE)  # Cloud
    ]

    obstacles_coordinates = [
        (50, 100),   # Tree
        (150, 200),  # Tree
        (250, 300),  # Tree
        (350, 100),  # Rock
        (450, 200),  # Rock
        (550, 300),  # Rock
        (150, 400),  # Bird
        (250, 500),  # Bird
        (350, 400),  # Bird
        (450, 500),  # Building
        (550, 100),  # Building
        (650, 200),  # Building
        (200, 350),  # Cloud
        (300, 450),  # Cloud
        (400, 550)   # Cloud
    ]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        parachute1.wind(1.1, 'right')
        parachute1.update()
        parachute2.wind(1.1, 'left')
        parachute2.update()

        if parachute1.detect_out_of_bounds() and parachute2.detect_out_of_bounds():
            end_screen(clock, home_screen_callback)

        screen.fill(WHITE)
        parachute1.draw(screen)
        parachute2.draw(screen)

        for obstacle, coord in zip(obstacles, obstacles_coordinates):
            obstacle.draw(coord, screen)

        pygame.display.flip()
        clock.tick(60)


def level_3(clock, home_screen_callback):
    clock = pygame.time.Clock()
    parachute1 = Parachute(1.8, pygame.K_LEFT, pygame.K_RIGHT)
    parachute2 = Parachute(1, pygame.K_a, pygame.K_d)
    
    obstacles = [
        Obstacle(RED),    # Tree
        Obstacle(RED),    # Tree
        Obstacle(RED),    # Tree
        Obstacle(RED),    # Tree
        Obstacle(BLUE),   # Rock
        Obstacle(BLUE),   # Rock
        Obstacle(BLUE),   # Rock
        Obstacle(BLUE),   # Rock
        Obstacle(YELLOW), # Bird
        Obstacle(YELLOW), # Bird
        Obstacle(YELLOW), # Bird
        Obstacle(YELLOW), # Bird
        Obstacle(GREEN),  # Building
        Obstacle(GREEN),  # Building
        Obstacle(GREEN),  # Building
        Obstacle(GREEN),  # Building
        Obstacle(PURPLE), # Cloud
        Obstacle(PURPLE), # Cloud
        Obstacle(PURPLE), # Cloud
        Obstacle(PURPLE), # Cloud
        Obstacle(RED),    # Additional Tree
        Obstacle(BLUE),   # Additional Rock
        Obstacle(YELLOW), # Additional Bird
        Obstacle(GREEN),  # Additional Building
        Obstacle(PURPLE)  # Additional Cloud
    ]
    
    obstacles_coordinates = [
        (50, 100),   # Tree
        (150, 200),  # Tree
        (250, 300),  # Tree
        (350, 100),  # Tree
        (450, 200),  # Rock
        (550, 300),  # Rock
        (150, 400),  # Rock
        (250, 500),  # Rock
        (350, 400),  # Bird
        (450, 500),  # Bird
        (550, 100),  # Bird
        (650, 200),  # Bird
        (200, 350),  # Building
        (300, 450),  # Building
        (400, 550),  # Building
        (500, 150),  # Building
        (100, 250),  # Cloud
        (200, 350),  # Cloud
        (300, 450),  # Cloud
        (400, 550),  # Cloud
        (700, 450),  # Additional Tree
        (600, 350),  # Additional Rock
        (700, 500),  # Additional Bird
        (750, 400),  # Additional Building
        (650, 550)   # Additional Cloud
    ]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        parachute1.wind(1.2, 'right')
        parachute1.update()
        parachute2.wind(1.2, 'left')
        parachute2.update()

        if parachute1.detect_out_of_bounds() and parachute2.detect_out_of_bounds():
            end_screen(clock, home_screen_callback)

        screen.fill(WHITE)
        parachute1.draw(screen)
        parachute2.draw(screen)

        for obstacle, coord in zip(obstacles, obstacles_coordinates):
            obstacle.draw(coord, screen)

        pygame.display.flip()
        clock.tick(60)


def start_level_1(clock, home_screen_callback):
    level_1(clock, home_screen_callback)

def start_level_2(clock, home_screen_callback):
    level_2(clock, home_screen_callback)

def start_level_3(clock, home_screen_callback):
    level_3(clock, home_screen_callback)
