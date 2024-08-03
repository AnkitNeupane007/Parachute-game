import pygame
import sys
import os
from settings import *
from parachute import Parachute
from obstacles import *
from end import end_screen

def level_1(clock, home_screen_callback, parachute_image):
    parachute1 = Parachute(2,100, 0, pygame.K_LEFT, pygame.K_RIGHT, parachute_image)
    parachute2 = Parachute(2, 600, 0, pygame.K_a, pygame.K_d, parachute_image)
    
    # Red: Xmas
    # Blue: Rock
    # Yellow: Bird
    # Green: Building
    # Purple: Cloud

    obstacles = [Obstacle(xmas_sp),  
                 Obstacle(rock_sp),                   
                 Obstacle(bird_sp),
                 Obstacle(building_sp),
                 Obstacle(cloud_sp),
                 Obstacle(rock_sp)]
    
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

        parachute1.update()
        parachute2.update()
        
        for obstacle, coord in zip(obstacles, obstacles_coordinates):
            obstacle.draw(coord, screen)
            print(obstacle.rect)

        if parachute1.detect_out_of_bounds() and parachute2.detect_out_of_bounds():
            end_screen(clock, home_screen_callback, GREEN)
            
        for obstacle, coord in zip(obstacles, obstacles_coordinates):
            if obstacle.detect_collision(parachute1) or obstacle.detect_collision(parachute2):
                end_screen(clock, home_screen_callback, RED)

        pygame.display.flip()
        clock.tick(60)

def level_2(clock, home_screen_callback, parachute_image):
    parachute1 = Parachute(0.5, 100, 0, pygame.K_LEFT, pygame.K_RIGHT, parachute_image)
    parachute2 = Parachute(0.5, 600, 0, pygame.K_a, pygame.K_d, parachute_image)

    obstacles = [
        Obstacle(xmas_sp),    # Tree
        Obstacle(xmas_sp),    # Tree
        Obstacle(xmas_sp),    # Tree
        Obstacle(rock_sp),   # Rock
        Obstacle(rock_sp),   # Rock
        Obstacle(rock_sp),   # Rock
        Obstacle(bird_sp), # Bird
        Obstacle(bird_sp), # Bird
        Obstacle(bird_sp), # Bird
        Obstacle(building_sp),  # Building
        Obstacle(building_sp),  # Building
        Obstacle(building_sp),  # Building
        Obstacle(cloud_sp), # Cloud
        Obstacle(cloud_sp), # Cloud
        Obstacle(cloud_sp)  # Cloud
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
                
        screen.fill(WHITE)
        screen.blit(level_background, screen.get_rect())
        parachute1.draw(screen)
        parachute2.draw(screen)

        parachute1.wind(0.8, 'right')
        parachute1.update()
        parachute2.wind(0.8, 'left')
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

def level_3(clock, home_screen_callback, parachute_image):
    clock = pygame.time.Clock()
    parachute1 = Parachute(1.8, 150, 0, pygame.K_LEFT, pygame.K_RIGHT, parachute_image)
    parachute2 = Parachute(1, 600, 0, pygame.K_a, pygame.K_d, parachute_image)

    obstacles = [
        Obstacle(xmas_sp),    # Tree
        Obstacle(xmas_sp),    # Tree
        Obstacle(xmas_sp),    # Tree
        Obstacle(xmas_sp),    # Tree
        Obstacle(rock_sp),   # Rock
        Obstacle(rock_sp),   # Rock
        Obstacle(rock_sp),   # Rock
        Obstacle(rock_sp),   # Rock
        Obstacle(bird_sp), # Bird
        Obstacle(bird_sp), # Bird
        Obstacle(bird_sp), # Bird
        Obstacle(bird_sp), # Bird
        Obstacle(building_sp),  # Building
        Obstacle(building_sp),  # Building
        Obstacle(building_sp),  # Building
        Obstacle(building_sp),  # Building
        Obstacle(cloud_sp), # Cloud
        Obstacle(cloud_sp), # Cloud
        Obstacle(cloud_sp), # Cloud
        Obstacle(cloud_sp), # Cloud
        Obstacle(xmas_sp),    # Additional Tree
        Obstacle(rock_sp),   # Additional Rock
        Obstacle(bird_sp), # Additional Bird
        Obstacle(building_sp),  # Additional Building
        Obstacle(cloud_sp)  # Additional Cloud
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
                
        screen.fill(WHITE)
        screen.blit(level_background, screen.get_rect())
        parachute1.draw(screen)
        parachute2.draw(screen)

        parachute1.wind(1.2, 'right')
        parachute1.update()
        parachute2.wind(1.2, 'left')
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
    buttons = [
        Button("PARACHUTE_1", 300, 300, GRAY, lambda: level_1(clock, home_screen_callback, PARACHUTE_1), PARACHUTE_1),
    ]
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            for button in buttons:
                button.check_click(event)  # Check for button clicks

        screen.fill(WHITE)
        for button in buttons:
            button.draw(screen)
            
        pygame.display.flip()
        clock.tick(60)
    
def start_level_2(clock, home_screen_callback):
    level_2(clock, home_screen_callback, PARACHUTE_3)

def start_level_3(clock, home_screen_callback):
    level_3(clock, home_screen_callback, PARACHUTE_4)
