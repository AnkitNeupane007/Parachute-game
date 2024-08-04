import pygame
import sys
import os
from settings import *
from parachute import Parachute
from obstacles import *
from end import end_screen
import random
from random import randint

def level_1(clock, home_screen_callback, parachute_image):
    parachute1 = Parachute(1.2,600, 0, pygame.K_LEFT, pygame.K_RIGHT, parachute_image)
    parachute2 = Parachute(1.2, 100, 0, pygame.K_a, pygame.K_d, parachute_image)
    
    # Red: Xmas
    # Blue: Bomb
    # Yellow: Skull-2
    # Green: Building
    # Purple: Skull-1

    obstacles = [Obstacle(xmas_sp),  
                 Obstacle(bomb_sp),                   
                 Obstacle(skull2_sp),
                 Obstacle(building_sp),
                 Obstacle(skull1_sp),
                 Obstacle(bomb_sp)]
    
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
                
        screen.fill(WHITE)
        screen.blit(level_background, screen.get_rect())
        
        parachute1.draw(screen)
        parachute2.draw(screen)

        parachute1.wind(random.uniform(0.3, 0.8), random.choice(wind_direction))
        parachute1.update()
        parachute2.wind(random.uniform(0.3, 0.8), random.choice(wind_direction))
        parachute2.update()
        
        for obstacle, coord in zip(obstacles, obstacles_coordinates):
            obstacle.draw(coord, screen)

        if parachute1.detect_out_of_bounds() and parachute2.detect_out_of_bounds():
            end_screen(clock, home_screen_callback, GREEN)
            
        for obstacle, coord in zip(obstacles, obstacles_coordinates):
            if obstacle.detect_collision(parachute1) or obstacle.detect_collision(parachute2):
                end_screen(clock, home_screen_callback, RED)

        pygame.display.flip()
        clock.tick(60)

def level_2(clock, home_screen_callback, parachute_image):
    clock = pygame.time.Clock()
    parachute1 = Parachute(1.4, randint(20, 300), 0, pygame.K_LEFT, pygame.K_RIGHT, parachute_image)
    # parachute2 = Parachute(0, 100, 0, pygame.K_a, pygame.K_d, parachute_image)

    obstacles = [
        Obstacle(xmas_sp),    # Tree
        Obstacle(xmas_sp),    # Tree
        Obstacle(xmas_sp),    # Tree
        Obstacle(bomb_sp),   # Bomb
        Obstacle(bomb_sp),   # Bomb
        Obstacle(bomb_sp),   # Bomb
        Obstacle(bomb_sp),   # Bomb
        Obstacle(skull2_sp), # Skull-2
        Obstacle(skull2_sp), # Skull-2
        Obstacle(skull2_sp), # Skull-2
        Obstacle(skull2_sp), # Skull-2
        Obstacle(building_sp),  # Building
        Obstacle(building_sp),  # Building
        Obstacle(building_sp),  # Building
        Obstacle(building_sp),  # Building
        Obstacle(skull1_sp), # Skull-1
        Obstacle(skull1_sp), # Skull-1
        Obstacle(xmas_sp),    # Additional Tree
        Obstacle(skull1_sp)  # Additional Skull-1
    ]
    
    obstacles_coordinates = [
        (50, 100),   # Tree
        (350, 300),  # Tree
        (350, 100),  # Tree
        (250, 200),  # Bomb
        (550, 300),  # Bomb
        (120, 450),  # Bomb
        (250, 500),  # Bomb
        (350, 400),  # Skull-2
        (750, 400),  # Skull-2
        (550, 100),  # Skull-2
        (650, 200),  # Skull-2
        (200, 350),  # Building
        (20, 550),  # Building
        (400, 550),  # Building
        (650, 550),  # Building
        (100, 250),  # Skull-1
        (20, 350),  # Skull-1
        (550, 450),  # Additional Tree
        (420, 200),   # Additional Skull-1
    ]

    direction = random.choice(wind_direction)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
        screen.fill(WHITE)
        screen.blit(level_background, screen.get_rect())
        parachute1.draw(screen)

        parachute1.wind(random.uniform(1.4, 1.9), direction)
        parachute1.update()

        
        for obstacle, coord in zip(obstacles, obstacles_coordinates):
            obstacle.draw(coord, screen)

        if parachute1.detect_out_of_bounds():
            end_screen(clock, home_screen_callback, GREEN)
            
        for obstacle, coord in zip(obstacles, obstacles_coordinates):
            if obstacle.detect_collision(parachute1):
                end_screen(clock, home_screen_callback, RED)

        pygame.display.flip()
        clock.tick(60)

def level_3(clock, home_screen_callback, parachute_image):
    parachute1 = Parachute(0.5, 600, 0, pygame.K_LEFT, pygame.K_RIGHT, parachute_image)
    parachute2 = Parachute(0.5, 100, 0, pygame.K_a, pygame.K_d, parachute_image)

    obstacles = [
        Obstacle(xmas_sp),    # Tree
        Obstacle(xmas_sp),    # Tree
        Obstacle(bomb_sp),   # Bomb
        Obstacle(bomb_sp),   # Bomb
        Obstacle(skull2_sp), # Skull-2
        Obstacle(skull2_sp), # Skull-2
        Obstacle(skull2_sp), # Skull-2
        Obstacle(building_sp),  # Building
        Obstacle(building_sp),  # Building
        Obstacle(building_sp),  # Building
        Obstacle(skull1_sp), # Skull-1
        Obstacle(skull1_sp), # Skull-1
        Obstacle(skull1_sp)  # Skull-1
    ]

    obstacles_coordinates = [
        (80, 280),  # Tree
        (300, 350),  # Tree
        (400, 150),  # Bomb
        (480, 260),  # Bomb
        (150, 420),  # Skull-2
        (520, 450),  # Skull-2
        (650, 150),  # Skull-2
        (100, 550),  # Building
        (350, 550),  # Building
        (650, 550),  # Building
        (50, 150),   # Skull-1
        (230, 200),  # Skull-1
        (680, 300),  # Skull-1
    ]
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
        screen.fill(WHITE)
        screen.blit(level_background, screen.get_rect())
        parachute1.draw(screen)
        parachute2.draw(screen)

        parachute1.wind(random.uniform(1.4, 1.9), 'left')
        parachute1.update()
        parachute2.wind(random.uniform(1.4, 1.9), 'right')
        parachute2.update()
        
        for obstacle, coord in zip(obstacles, obstacles_coordinates):
            obstacle.draw(coord, screen)

        if parachute1.detect_out_of_bounds() and parachute2.detect_out_of_bounds():
            end_screen(clock, home_screen_callback, GREEN)
            
        for obstacle, coord in zip(obstacles, obstacles_coordinates):
            if obstacle.detect_collision(parachute1) or obstacle.detect_collision(parachute2):
                end_screen(clock, home_screen_callback, RED)

        pygame.display.flip()
        clock.tick(60)

def start_level_1(clock, home_screen_callback):
    button_size = 80
    buttons = [
        Button("1", 350, 150, button_size, button_size, GRAY, lambda: level_1(clock, home_screen_callback, PARACHUTE_1), PARACHUTE_1),
        Button("2", 350, 250, button_size, button_size, LIGHT_WHITE, lambda: level_1(clock, home_screen_callback, PARACHUTE_2), PARACHUTE_2),
        Button("3", 350, 350, button_size, button_size, RED, lambda: level_1(clock, home_screen_callback, PARACHUTE_3), PARACHUTE_3),
    ]
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            for button in buttons:
                button.check_click(event)  # Check for button clicks

        screen.fill(WHITE)
        screen.blit(level_background, home_screen_image.get_rect())

        
        for button in buttons:
            button.display(screen)
            
        pygame.display.flip()
        clock.tick(60)
    
def start_level_2(clock, home_screen_callback):
    button_size = 80
    buttons = [
        Button("4", 350, 150, button_size, button_size, GRAY, lambda: level_2(clock, home_screen_callback, PARACHUTE_4), PARACHUTE_4),
        Button("5", 350, 250, button_size, button_size, LIGHT_WHITE, lambda: level_2(clock, home_screen_callback, PARACHUTE_5), PARACHUTE_5),
        # Button("3", 350, 350, button_size, button_size, RED, lambda: level_2(clock, home_screen_callback, PARACHUTE_3), PARACHUTE_3),
    ]
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            for button in buttons:
                button.check_click(event)  # Check for button clicks

        screen.fill(WHITE)
        screen.blit(level_background, home_screen_image.get_rect())

        
        for button in buttons:
            button.display(screen)
            
        pygame.display.flip()
        clock.tick(60)

def start_level_3(clock, home_screen_callback):
    level_3(clock, home_screen_callback, PARACHUTE_4)
