from settings import *
import sys

def end_screen(clock, home_screen_callback, color, level_callback):
    button_width = SCREEN_WIDTH * 0.15625  # Example: 125 / 800
    button_height = SCREEN_HEIGHT * 0.075  # Example: 45 / 600
    
    buttons = [
        Button("Home", SCREEN_WIDTH * 0.3125, SCREEN_HEIGHT * 0.5, button_width, button_height, GRAY, lambda: home_screen_callback(clock)),
        Button("Restart Level", SCREEN_WIDTH * 0.5, SCREEN_HEIGHT * 0.5, button_width * 1.6, button_height, GRAY, lambda: level_callback(clock, home_screen_callback))
    ]
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            for button in buttons:
                button.check_click(event)

        screen.fill(color)

        if color == GREEN:
            game_over_text = font.render("You Win!", True, BLACK)
        else:
            game_over_text = font.render("Game Over", True, WHITE)
        
        screen.blit(game_over_text, (SCREEN_WIDTH // 2 - game_over_text.get_width() // 2, SCREEN_HEIGHT * 0.3333))

        for button in buttons:
            button.draw(screen)
        pygame.display.flip()

        clock.tick(60)
