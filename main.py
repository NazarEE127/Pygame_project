import pygame
from go_interface import display_game_over  # Импортируем функцию из go_interface

# Инициализация Pygame
pygame.init()

# Настройки экрана
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Springendefaust")

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Персонаж
bird_rect = pygame.Rect(50, 300, 30, 30)  # Позиция и размеры персонажа
bird_velocity = 0
gravity = 0.5

obstacle_width = 70
obstacle_height = 400  # Высота стены
obstacle_rect = pygame.Rect(WIDTH, HEIGHT - obstacle_height, obstacle_width, obstacle_height)

# Функция проверки столкновений
def check_collision(bird_rect, obstacle_rect):
    return bird_rect.colliderect(obstacle_rect)

# Основной игровой цикл
running = True
game_over = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Обработка нажатия клавиши пробела или стрелочки вверх для прыжка
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not game_over:
                bird_velocity = -8  # Прыжок
            elif event.key == pygame.K_UP and not game_over:
                bird_velocity = -8  # Прыжок

        # Обработка нажатия мыши для прыжка
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            bird_velocity = -8  # Прыжок

    if not game_over:
        # Применение гравитации к персонажу
        bird_velocity += gravity
        bird_rect.y += bird_velocity

        # Движение препятствия
        obstacle_rect.x -= 5  # Скорость движения препятствия влево

        # Проверка на столкновение или выход за пределы экрана
        if check_collision(bird_rect, obstacle_rect) or bird_rect.y > HEIGHT or bird_rect.y < 0:
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