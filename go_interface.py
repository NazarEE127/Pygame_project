import pygame

# Надпись "Игра окончена"
def display_game_over(screen, width, height):
    font = pygame.font.Font(None, 74)
    text_surface = font.render("Игра окончена", True, (255, 0, 0))
    text_rect = text_surface.get_rect(center=(width // 2, height // 2))
    screen.blit(text_surface, text_rect)