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
    parachute1 = Parachute(1.5, SCREEN_WIDTH * 0.75, 0, pygame.K_LEFT, pygame.K_RIGHT, parachute_image)
    parachute2 = Parachute(1.5, SCREEN_WIDTH * 0.125, 0, pygame.K_a, pygame.K_d, parachute_image)
    
    obstacles = [Obstacle(xmas_sp),  
                 Obstacle(bomb_sp),                   
                 Obstacle(skull2_sp),
                 Obstacle(building_sp),
                 Obstacle(skull1_sp),
                 Obstacle(bomb_sp)]
    
    obstacles_coordinates = [(SCREEN_WIDTH * 0.125, SCREEN_HEIGHT * 0.5),
                             (SCREEN_WIDTH * 0.6, SCREEN_HEIGHT * 0.4167),
                             (SCREEN_WIDTH * 0.3125, SCREEN_HEIGHT * 0.5833),
                             (SCREEN_WIDTH * 0.5625, SCREEN_HEIGHT * 0.8333),
                             (SCREEN_WIDTH * 0.6875, SCREEN_HEIGHT * 0.1667),
                             (SCREEN_WIDTH * 0.8125, SCREEN_HEIGHT * 0.6667)]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
        screen.fill(WHITE)
        screen.blit(level_background, screen.get_rect())
        
        parachute1.draw(screen)
        parachute2.draw(screen)

        parachute1.update()
        parachute2.update()
        
        for obstacle, coord in zip(obstacles, obstacles_coordinates):
            obstacle.draw(coord, screen)

        if parachute1.detect_out_of_bounds() and parachute2.detect_out_of_bounds():
            end_screen(clock, home_screen_callback, GREEN, start_level_1)
            
        for obstacle, coord in zip(obstacles, obstacles_coordinates):
            if obstacle.detect_collision(parachute1) or obstacle.detect_collision(parachute2):
                end_screen(clock, home_screen_callback, RED, start_level_1)

        pygame.display.flip()
        clock.tick(60)

def level_2(clock, home_screen_callback, parachute_image):
    parachute1 = Parachute(1.4, random.uniform(SCREEN_WIDTH * 0.025, SCREEN_WIDTH * 0.375), 0, pygame.K_LEFT, pygame.K_RIGHT, parachute_image)

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
        (SCREEN_WIDTH * 0.0625, SCREEN_HEIGHT * 0.1667),   # Tree
        (SCREEN_WIDTH * 0.4375, SCREEN_HEIGHT * 0.5),  # Tree
        (SCREEN_WIDTH * 0.4375, SCREEN_HEIGHT * 0.1667),  # Tree
        (SCREEN_WIDTH * 0.3125, SCREEN_HEIGHT * 0.3333),  # Bomb
        (SCREEN_WIDTH * 0.6875, SCREEN_HEIGHT * 0.5),  # Bomb
        (SCREEN_WIDTH * 0.15, SCREEN_HEIGHT * 0.75),  # Bomb
        (SCREEN_WIDTH * 0.3125, SCREEN_HEIGHT * 0.8333),  # Bomb
        (SCREEN_WIDTH * 0.4375, SCREEN_HEIGHT * 0.6667),  # Skull-2
        (SCREEN_WIDTH * 0.9375, SCREEN_HEIGHT * 0.6667),  # Skull-2
        (SCREEN_WIDTH * 0.6875, SCREEN_HEIGHT * 0.1667),  # Skull-2
        (SCREEN_WIDTH * 0.8125, SCREEN_HEIGHT * 0.3333),  # Skull-2
        (SCREEN_WIDTH * 0.25, SCREEN_HEIGHT * 0.5833),  # Building
        (SCREEN_WIDTH * 0.025, SCREEN_HEIGHT * 0.9167),  # Building
        (SCREEN_WIDTH * 0.5, SCREEN_HEIGHT * 0.9167),  # Building
        (SCREEN_WIDTH * 0.8125, SCREEN_HEIGHT * 0.9167),  # Building
        (SCREEN_WIDTH * 0.125, SCREEN_HEIGHT * 0.4167),  # Skull-1
        (SCREEN_WIDTH * 0.025, SCREEN_HEIGHT * 0.5833),  # Skull-1
        (SCREEN_WIDTH * 0.6875, SCREEN_HEIGHT * 0.75),  # Additional Tree
        (SCREEN_WIDTH * 0.525, SCREEN_HEIGHT * 0.3333),   # Additional Skull-1
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
            end_screen(clock, home_screen_callback, GREEN, start_level_2)
            
        for obstacle, coord in zip(obstacles, obstacles_coordinates):
            if obstacle.detect_collision(parachute1):
                end_screen(clock, home_screen_callback, RED, start_level_2)

        pygame.display.flip()
        clock.tick(60)

def level_3(clock, home_screen_callback, parachute_image):
    parachute1 = Parachute(0.5, SCREEN_WIDTH * 0.75, 0, pygame.K_LEFT, pygame.K_RIGHT, parachute_image)
    parachute2 = Parachute(0.5, SCREEN_WIDTH * 0.125, 0, pygame.K_a, pygame.K_d, parachute_image)

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
        Obstacle(skull1_sp),  # Skull-1
        Obstacle(skull1_sp),  # Skull-1
        Obstacle(bomb_sp),  # Skull-1
    ]

    obstacles_coordinates = [
        (SCREEN_WIDTH * 0.1, SCREEN_HEIGHT * 0.4667),  # Tree
        (SCREEN_WIDTH * 0.375, SCREEN_HEIGHT * 0.5833),  # Tree
        (SCREEN_WIDTH * 0.5, SCREEN_HEIGHT * 0.25),  # Bomb
        (SCREEN_WIDTH * 0.6, SCREEN_HEIGHT * 0.4333),  # Bomb
        (SCREEN_WIDTH * 0.1875, SCREEN_HEIGHT * 0.7),  # Skull-2
        (SCREEN_WIDTH * 0.65, SCREEN_HEIGHT * 0.75),  # Skull-2
        (SCREEN_WIDTH * 0.8125, SCREEN_HEIGHT * 0.25),  # Skull-2
        (SCREEN_WIDTH * 0.125, SCREEN_HEIGHT * 0.9167),  # Building
        (SCREEN_WIDTH * 0.4375, SCREEN_HEIGHT * 0.9167),  # Building
        (SCREEN_WIDTH * 0.8125, SCREEN_HEIGHT * 0.9167),  # Building
        (SCREEN_WIDTH * 0.0625, SCREEN_HEIGHT * 0.25),   # Skull-1
        (SCREEN_WIDTH * 0.2875, SCREEN_HEIGHT * 0.3333),  # Skull-1
        (SCREEN_WIDTH * 0.85, SCREEN_HEIGHT * 0.5),  # Skull-1
        (SCREEN_WIDTH * 0.025, SCREEN_HEIGHT * 0.75),  # Skull-1
        (SCREEN_WIDTH * 0.9125, SCREEN_HEIGHT * 0.7167),  # Skull-1
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
            end_screen(clock, home_screen_callback, GREEN, start_level_3)
            
        for obstacle, coord in zip(obstacles, obstacles_coordinates):
            if obstacle.detect_collision(parachute1) or obstacle.detect_collision(parachute2):
                end_screen(clock, home_screen_callback, RED, start_level_3)

        pygame.display.flip()
        clock.tick(60)

def start_level_1(clock, home_screen_callback):
    button_size = 80
    buttons = [
        Button("1", SCREEN_WIDTH * 0.4375, SCREEN_HEIGHT * 0.25, button_size, button_size, GRAY, lambda: level_1(clock, home_screen_callback, PARACHUTE_1), PARACHUTE_1),
        Button("2", SCREEN_WIDTH * 0.4375, SCREEN_HEIGHT * 0.4167, button_size, button_size, LIGHT_WHITE, lambda: level_1(clock, home_screen_callback, PARACHUTE_2), PARACHUTE_2),
        Button("3", SCREEN_WIDTH * 0.4375, SCREEN_HEIGHT * 0.5833, button_size, button_size, RED, lambda: level_1(clock, home_screen_callback, PARACHUTE_3), PARACHUTE_3),
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
        Button("4", SCREEN_WIDTH * 0.4375, SCREEN_HEIGHT * 0.25, button_size, button_size, GRAY, lambda: level_2(clock, home_screen_callback, PARACHUTE_4), PARACHUTE_4),
        Button("5", SCREEN_WIDTH * 0.4375, SCREEN_HEIGHT * 0.4167, button_size, button_size, LIGHT_WHITE, lambda: level_2(clock, home_screen_callback, PARACHUTE_5), PARACHUTE_5),
        # Button("3", SCREEN_WIDTH * 0.4375, SCREEN_HEIGHT * 0.5833, button_size, button_size, RED, lambda: level_2(clock, home_screen_callback, PARACHUTE_3), PARACHUTE_3),
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
    level_3(clock, home_screen_callback, PARACHUTE_100)