import pygame
from go_interface import display_game_over

# Инициализация Pygame
pygame.init()

# Настройки экрана
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird Clone")

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Персонаж
bird_rect = pygame.Rect(50, 300, 30, 30)  # Позиция и размеры персонажа

# Препятствие (сплошная стена)
obstacle_width = 70
obstacle_height = 400  # Высота стены
obstacle_rect = pygame.Rect(WIDTH, HEIGHT - obstacle_height, obstacle_width, obstacle_height)

def check_collision(bird_rect, obstacle_rect):
    return bird_rect.colliderect(obstacle_rect)

# Основной игровой цикл
running = True
game_over = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not game_over:
        # Движение препятствия
        obstacle_rect.x -= 5  # Скорость движения препятствия влево

        # Проверка на столкновение
        if check_collision(bird_rect, obstacle_rect):
            game_over = True

        # Отрисовка объектов на экране
        screen.fill(WHITE)
        pygame.draw.rect(screen, BLACK, bird_rect)  # Отрисовка персонажа
        pygame.draw.rect(screen, BLACK, obstacle_rect)  # Отрисовка стены

    else:
        # Вызов функции для отображения сообщения "Игра окончена"
        display_game_over(screen, WIDTH, HEIGHT)

    pygame.display.flip()
    pygame.time.delay(30)

pygame.quit()