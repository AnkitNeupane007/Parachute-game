from settings import *
import sys

def end_screen(clock, home_screen_callback, color, level_callback):
    buttons = [
        Button("Home", 250, 300, 125, 45, GRAY, lambda: home_screen_callback(clock)),
        Button("Restart Level", 400, 300, 200, 45, GRAY, lambda: level_callback(clock, home_screen_callback))
    ]
    
    # if level:
    #     buttons.append(
    #         Button("Restart Level", 450, 300, 130, 45,GRAY, lambda: level(clock, home_screen_callback))
    #     )

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
