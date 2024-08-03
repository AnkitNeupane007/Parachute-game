from settings import *
import sys

def end_screen(clock, home_screen_callback, color):
    buttons = [
        Button("Home", 300, 300, GRAY, lambda: home_screen_callback(clock)),
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
        
        screen.blit(game_over_text, (SCREEN_WIDTH // 2 - game_over_text.get_width() // 2, 200))

        for button in buttons:
            button.draw(screen)
        pygame.display.flip()

        clock.tick(60)
