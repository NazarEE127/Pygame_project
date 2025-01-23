import pygame
from go_interface import display_game_over  # Импортируем функцию из go_interface
import random

# Инициализация Pygame
pygame.init()

# Настройки экрана
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# # Персонаж
# bird_rect = pygame.Rect(50, 300, 30, 30)  # Позиция и размеры персонажа
# bird_velocity = 0
# gravity = 0.5
#
# obstacle_width = 70
# obstacle_height = 400  # Высота стены
# obstacle_rect = pygame.Rect(WIDTH, HEIGHT - obstacle_height, obstacle_width, obstacle_height)

# Настройки игры
gravity = 0.5
bird_movement = 0
game_active = True
score = 0

# Загрузка изображений
bird_surface = pygame.Surface((34, 24))
bird_surface.fill(BLUE)

pipe_surface = pygame.Surface((52, 400))
pipe_surface.fill(GREEN)

# Создание труб
def create_pipe():
    height = random.randint(200, 400)
    bottom_pipe = pipe_surface.get_rect(midtop=(500, height))
    top_pipe = pipe_surface.get_rect(midbottom=(500, height - 150))
    return bottom_pipe, top_pipe

# Движение труб
def move_pipes(pipes):
    for pipe in pipes:
        pipe.centerx -= 5
    return pipes

# Отображение труб на экране
def draw_pipes(pipes):
    for pipe in pipes:
        if pipe.bottom >= HEIGHT:
            screen.blit(pipe_surface, pipe)
        else:
            flipped_pipe = pygame.transform.flip(pipe_surface, False, True)
            screen.blit(flipped_pipe, pipe)

# Проверка столкновений
def check_collision(pipes):
    for pipe in pipes:
        if bird_rect.colliderect(pipe):
            return False
    if bird_rect.top <= -50 or bird_rect.bottom >= HEIGHT:
        return False
    return True

# # Функция проверки столкновений
# def check_collision(bird_rect, obstacle_rect):
#     return bird_rect.colliderect(obstacle_rect)

# # Основной игровой цикл
# running = True
# game_over = False
#
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#
#         # Обработка нажатия клавиши пробела или стрелочки вверх для прыжка
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_SPACE and not game_over:
#                 bird_velocity = -8  # Прыжок
#             elif event.key == pygame.K_UP and not game_over:
#                 bird_velocity = -8  # Прыжок
#
#         # Обработка нажатия мыши для прыжка
#         if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
#             bird_velocity = -8  # Прыжок
#
#     if not game_over:
#         # Применение гравитации к персонажу
#         bird_velocity += gravity
#         bird_rect.y += bird_velocity
#
#         # Движение препятствия
#         obstacle_rect.x -= 5  # Скорость движения препятствия влево
#
#         # Проверка на столкновение или выход за пределы экрана
#         if check_collision(bird_rect, obstacle_rect) or bird_rect.y > HEIGHT or bird_rect.y < 0:
#             game_over = True
#
#         # Отрисовка объектов на экране
#         screen.fill(WHITE)
#         pygame.draw.rect(screen, BLACK, bird_rect)  # Отрисовка персонажа
#         pygame.draw.rect(screen, BLACK, obstacle_rect)  # Отрисовка стены
#
#     else:
#         # Вызов функции для отображения сообщения "Игра окончена"
#         display_game_over(screen, WIDTH, HEIGHT)
#
#     pygame.display.flip()
#     pygame.time.delay(30)
#
# pygame.quit()

# Основной игровой цикл
clock = pygame.time.Clock()
bird_rect = bird_surface.get_rect(center=(100, HEIGHT // 2))
pipes = []
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE, 1200)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_active:
                bird_movement = 0
                bird_movement -= 10
            if event.key == pygame.K_SPACE and not game_active:
                game_active = True
                pipes.clear()
                bird_rect.center = (100, HEIGHT // 2)
                bird_movement = 0
                score = 0
            if event.key == pygame.K_UP and game_active:
                bird_movement = 0
                bird_movement -= 10
            if event.key == pygame.K_UP and not game_active:
                game_active = True
                pipes.clear()
                bird_rect.center = (100, HEIGHT // 2)
                bird_movement = 0
                score = 0

        # Обработка нажатия мыши для прыжка
        if event.type == pygame.MOUSEBUTTONDOWN and game_active:
            bird_movement = 0
            bird_movement -= 10  # Прыжок
        if event.type == pygame.MOUSEBUTTONDOWN and not game_active:
            game_active = True
            pipes.clear()
            bird_rect.center = (100, HEIGHT // 2)
            bird_movement = 0
            score = 0

        if event.type == SPAWNPIPE:
            pipes.extend(create_pipe())

    screen.fill(WHITE)

    if game_active:
        # Движение птицы
        bird_movement += gravity
        bird_rect.centery += bird_movement
        game_active = check_collision(pipes)

        # Отображение птицы и труб
        screen.blit(bird_surface, bird_rect)
        pipes = move_pipes(pipes)
        draw_pipes(pipes)

    else:
        display_game_over(screen, WIDTH, HEIGHT)  # Вызов функции для отображения сообщения "Игра окончена"

    pygame.display.flip()
    clock.tick(120)
