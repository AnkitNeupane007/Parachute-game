import pygame
import sys
import os
from settings import *
from parachute import Parachute
from obstacles import *
from end import end_screen
import random
from random import randint

BUTTON_SIZE = 80

OBSTACLES_LEVEL_1 = [
    (Obstacle(xmas_sp), (SCREEN_WIDTH * 0.125, SCREEN_HEIGHT * 0.5)),
    (Obstacle(bomb_sp), (SCREEN_WIDTH * 0.6, SCREEN_HEIGHT * 0.4167)),
    (Obstacle(skull2_sp), (SCREEN_WIDTH * 0.3125, SCREEN_HEIGHT * 0.5833)),
    (Obstacle(building_sp), (SCREEN_WIDTH * 0.5625, SCREEN_HEIGHT * 0.8333)),
    (Obstacle(skull1_sp), (SCREEN_WIDTH * 0.6875, SCREEN_HEIGHT * 0.1667)),
    (Obstacle(bomb_sp), (SCREEN_WIDTH * 0.8125, SCREEN_HEIGHT * 0.6667))
]

OBSTACLES_LEVEL_2 = [
    (Obstacle(xmas_sp), (SCREEN_WIDTH * 0.0625, SCREEN_HEIGHT * 0.1667)),
    (Obstacle(xmas_sp), (SCREEN_WIDTH * 0.4375, SCREEN_HEIGHT * 0.5)),
    (Obstacle(xmas_sp), (SCREEN_WIDTH * 0.4375, SCREEN_HEIGHT * 0.1667)),
    (Obstacle(bomb_sp), (SCREEN_WIDTH * 0.3125, SCREEN_HEIGHT * 0.3333)),
    (Obstacle(bomb_sp), (SCREEN_WIDTH * 0.6875, SCREEN_HEIGHT * 0.5)),
    (Obstacle(bomb_sp), (SCREEN_WIDTH * 0.15, SCREEN_HEIGHT * 0.75)),
    (Obstacle(bomb_sp), (SCREEN_WIDTH * 0.3125, SCREEN_HEIGHT * 0.8333)),
    (Obstacle(skull2_sp), (SCREEN_WIDTH * 0.4375, SCREEN_HEIGHT * 0.6667)),
    (Obstacle(skull2_sp), (SCREEN_WIDTH * 0.9375, SCREEN_HEIGHT * 0.6667)),
    (Obstacle(skull2_sp), (SCREEN_WIDTH * 0.6875, SCREEN_HEIGHT * 0.1667)),
    (Obstacle(skull2_sp), (SCREEN_WIDTH * 0.8125, SCREEN_HEIGHT * 0.3333)),
    (Obstacle(building_sp), (SCREEN_WIDTH * 0.25, SCREEN_HEIGHT * 0.5833)),
    (Obstacle(building_sp), (SCREEN_WIDTH * 0.025, SCREEN_HEIGHT * 0.9167)),
    (Obstacle(building_sp), (SCREEN_WIDTH * 0.5, SCREEN_HEIGHT * 0.9167)),
    (Obstacle(building_sp), (SCREEN_WIDTH * 0.8125, SCREEN_HEIGHT * 0.9167)),
    (Obstacle(skull1_sp), (SCREEN_WIDTH * 0.125, SCREEN_HEIGHT * 0.4167)),
    (Obstacle(skull1_sp), (SCREEN_WIDTH * 0.025, SCREEN_HEIGHT * 0.5833)),
    (Obstacle(xmas_sp), (SCREEN_WIDTH * 0.6875, SCREEN_HEIGHT * 0.75)),
    (Obstacle(skull1_sp), (SCREEN_WIDTH * 0.525, SCREEN_HEIGHT * 0.3333))
]

OBSTACLES_LEVEL_3 = [
    (Obstacle(xmas_sp), (SCREEN_WIDTH * 0.1, SCREEN_HEIGHT * 0.4667)),
    (Obstacle(xmas_sp), (SCREEN_WIDTH * 0.375, SCREEN_HEIGHT * 0.5833)),
    (Obstacle(bomb_sp), (SCREEN_WIDTH * 0.5, SCREEN_HEIGHT * 0.25)),
    (Obstacle(bomb_sp), (SCREEN_WIDTH * 0.6, SCREEN_HEIGHT * 0.4333)),
    (Obstacle(skull2_sp), (SCREEN_WIDTH * 0.1875, SCREEN_HEIGHT * 0.7)),
    (Obstacle(skull2_sp), (SCREEN_WIDTH * 0.65, SCREEN_HEIGHT * 0.75)),
    (Obstacle(skull2_sp), (SCREEN_WIDTH * 0.8125, SCREEN_HEIGHT * 0.25)),
    (Obstacle(building_sp), (SCREEN_WIDTH * 0.125, SCREEN_HEIGHT * 0.9167)),
    (Obstacle(building_sp), (SCREEN_WIDTH * 0.4375, SCREEN_HEIGHT * 0.9167)),
    (Obstacle(building_sp), (SCREEN_WIDTH * 0.8125, SCREEN_HEIGHT * 0.9167)),
    (Obstacle(skull1_sp), (SCREEN_WIDTH * 0.0625, SCREEN_HEIGHT * 0.25)),
    (Obstacle(skull1_sp), (SCREEN_WIDTH * 0.2875, SCREEN_HEIGHT * 0.3333)),
    (Obstacle(skull1_sp), (SCREEN_WIDTH * 0.85, SCREEN_HEIGHT * 0.5)),
    (Obstacle(skull1_sp), (SCREEN_WIDTH * 0.025, SCREEN_HEIGHT * 0.75)),
    (Obstacle(bomb_sp), (SCREEN_WIDTH * 0.9125, SCREEN_HEIGHT * 0.7167))
]

def draw_and_update_parachutes(parachutes):
    for parachute in parachutes:
        parachute.draw(screen)
        parachute.update()

def draw_obstacles(obstacles):
    for obstacle, coord in obstacles:
        obstacle.draw(coord, screen)

def check_collision(parachutes, obstacles, callback, clock, home_screen_callback, color, level_start):
    if all(p.detect_out_of_bounds() for p in parachutes):
        end_screen(clock, home_screen_callback, color, level_start)
        
    for parachute in parachutes:
        for obstacle, _ in obstacles:
            if obstacle.detect_collision(parachute):
                end_screen(clock, home_screen_callback, RED, level_start)

def level_1(clock, home_screen_callback, parachute_image):
    parachute1 = Parachute(1.5, SCREEN_WIDTH * 0.75, 0, pygame.K_LEFT, pygame.K_RIGHT, parachute_image)
    parachute2 = Parachute(1.5, SCREEN_WIDTH * 0.125, 0, pygame.K_a, pygame.K_d, parachute_image)
    parachutes = [parachute1, parachute2]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
        screen.fill(WHITE)
        screen.blit(level_background, screen.get_rect())

        draw_and_update_parachutes(parachutes)
        draw_obstacles(OBSTACLES_LEVEL_1)
        check_collision(parachutes, OBSTACLES_LEVEL_1, end_screen, clock, home_screen_callback, GREEN, start_level_1)

        pygame.display.flip()
        clock.tick(60)

def level_2(clock, home_screen_callback, parachute_image):
    parachute1 = Parachute(1.4, random.uniform(SCREEN_WIDTH * 0.025, SCREEN_WIDTH * 0.375), 0, pygame.K_LEFT, pygame.K_RIGHT, parachute_image)
    parachutes = [parachute1]

    direction = random.choice(wind_direction)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
        screen.fill(WHITE)
        screen.blit(level_background, screen.get_rect())

        parachute1.wind(random.uniform(1.4, 1.9), direction)
        draw_and_update_parachutes(parachutes)
        draw_obstacles(OBSTACLES_LEVEL_2)
        check_collision(parachutes, OBSTACLES_LEVEL_2, end_screen, clock, home_screen_callback, GREEN, start_level_2)

        pygame.display.flip()
        clock.tick(60)

def level_3(clock, home_screen_callback, parachute_image):
    parachute1 = Parachute(0.5, SCREEN_WIDTH * 0.75, 0, pygame.K_LEFT, pygame.K_RIGHT, parachute_image)
    parachute2 = Parachute(0.5, SCREEN_WIDTH * 0.125, 0, pygame.K_a, pygame.K_d, parachute_image)
    parachutes = [parachute1, parachute2]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
        screen.fill(WHITE)
        screen.blit(level_background, screen.get_rect())

        parachute1.wind(random.uniform(1.4, 1.9), 'left')
        parachute2.wind(random.uniform(1.4, 1.9), 'right')
        draw_and_update_parachutes(parachutes)
        draw_obstacles(OBSTACLES_LEVEL_3)
        check_collision(parachutes, OBSTACLES_LEVEL_3, end_screen, clock, home_screen_callback, GREEN, start_level_3)

        pygame.display.flip()
        clock.tick(60)

def start_level_1(clock, home_screen_callback):
    buttons = [
        Button("1", SCREEN_WIDTH * 0.4375, SCREEN_HEIGHT * 0.25, BUTTON_SIZE, BUTTON_SIZE, GRAY, lambda: level_1(clock, home_screen_callback, PARACHUTE_1), PARACHUTE_1),
        Button("2", SCREEN_WIDTH * 0.4375, SCREEN_HEIGHT * 0.4167, BUTTON_SIZE, BUTTON_SIZE, LIGHT_WHITE, lambda: level_1(clock, home_screen_callback, PARACHUTE_2), PARACHUTE_2),
        Button("3", SCREEN_WIDTH * 0.4375, SCREEN_HEIGHT * 0.5833, BUTTON_SIZE, BUTTON_SIZE, RED, lambda: level_1(clock, home_screen_callback, PARACHUTE_3), PARACHUTE_3),
    ]
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            for button in buttons:
                button.check_click(event)

        screen.fill(WHITE)
        screen.blit(level_background, home_screen_image.get_rect())

        for button in buttons:
            button.display(screen)
            
        pygame.display.flip()
        clock.tick(60)

def start_level_2(clock, home_screen_callback):
    buttons = [
        Button("4", SCREEN_WIDTH * 0.4375, SCREEN_HEIGHT * 0.25, BUTTON_SIZE, BUTTON_SIZE, GRAY, lambda: level_2(clock, home_screen_callback, PARACHUTE_4), PARACHUTE_4),
        Button("5", SCREEN_WIDTH * 0.4375, SCREEN_HEIGHT * 0.4167, BUTTON_SIZE, BUTTON_SIZE, LIGHT_WHITE, lambda: level_2(clock, home_screen_callback, PARACHUTE_5), PARACHUTE_5),
    ]
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            for button in buttons:
                button.check_click(event)

        screen.fill(WHITE)
        screen.blit(level_background, home_screen_image.get_rect())

        for button in buttons:
            button.display(screen)
            
        pygame.display.flip()
        clock.tick(60)

def start_level_3(clock, home_screen_callback):
    level_3(clock, home_screen_callback, PARACHUTE_100)
