import pygame
import sys
from settings import *
from parachute import Parachute
from obstacles import *
from end import end_screen

def level_1(clock, home_screen_callback):
    parachute1 = Parachute(2, pygame.K_LEFT, pygame.K_RIGHT)
    parachute2 = Parachute(2, pygame.K_a, pygame.K_d)
    
    obstacles = [Obstacle(RED),
                 Obstacle(RED),
                 Obstacle(RED)]
    
    obstacles_coordinates = [(200, 300),
                             (250, 350),
                             (450, 550)]

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
    parachute = Parachute(4, pygame.K_LEFT, pygame.K_RIGHT)
    obstacles = [Obstacle(200, 300, 50, 50, RED), Obstacle(400, 500, 50, 50, RED)]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        parachute.update()
        if parachute.detect_out_of_bounds():
            end_screen(clock, home_screen_callback)

        screen.fill(WHITE)
        parachute.draw(screen)

        for obstacle in obstacles:
            obstacle.draw(screen)

        pygame.display.flip()
        clock.tick(60)

def level_3(clock, home_screen_callback):
    parachute = Parachute(6, pygame.K_LEFT, pygame.K_RIGHT)
    obstacles = [Obstacle(100, 200, 50, 50, RED), Obstacle(300, 400, 50, 50, RED), Obstacle(500, 600, 50, 50, RED)]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        parachute.update()
        if parachute.detect_out_of_bounds():
            end_screen(clock, home_screen_callback)

        screen.fill(WHITE)
        parachute.draw(screen)

        for obstacle in obstacles:
            obstacle.draw(screen)

        pygame.display.flip()
        clock.tick(60)

def start_level_1(clock, home_screen_callback):
    level_1(clock, home_screen_callback)

def start_level_2(clock, home_screen_callback):
    level_2(clock, home_screen_callback)

def start_level_3(clock, home_screen_callback):
    level_3(clock, home_screen_callback)
