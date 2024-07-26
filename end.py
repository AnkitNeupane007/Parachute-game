from settings import *

def end_screen(clock, home_screen_callback):
    buttons = [
        Button("Home", 300, 300, WHITE, lambda: home_screen_callback(clock)),
    ]

    while True:#gg
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            for button in buttons:
                button.check_click(event)

        screen.fill(GREEN)

        game_over_text = font.render("Game Over", True, WHITE)
        screen.blit(game_over_text, (SCREEN_WIDTH // 2 - game_over_text.get_width() // 2, 200))

        for button in buttons:
            button.draw(screen)
        pygame.display.flip()

        clock.tick(60)
