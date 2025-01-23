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


# Настройки игры
GRAVITY = 0.5
bird_movement = 0
game_active = True
score = 0

# Константы
BIRD_WIDTH = 34
BIRD_HEIGHT = 24
PIPE_WIDTH = 70
PIPE_HEIGHT = 500
FLAP_STRENGTH = -10

# Загрузка изображений
bird_surface = pygame.Surface((34, 24))
bird_surface.fill(BLUE)

pipe_surface = pygame.Surface((52, 400))
pipe_surface.fill(GREEN)

# # Создание труб
# def create_pipe():
#     height = random.randint(200, 400)
#     bottom_pipe = pipe_surface.get_rect(midtop=(500, height))
#     top_pipe = pipe_surface.get_rect(midbottom=(500, height - 150))
#     return bottom_pipe, top_pipe
#
# # Движение труб
# def move_pipes(pipes):
#     for pipe in pipes:
#         pipe.centerx -= 5
#     return pipes
#
# # Отображение труб на экране
# def draw_pipes(pipes):
#     for pipe in pipes:
#         if pipe.bottom >= HEIGHT:
#             screen.blit(pipe_surface, pipe)
#         else:
#             flipped_pipe = pygame.transform.flip(pipe_surface, False, True)
#             screen.blit(flipped_pipe, pipe)
#
# # Проверка столкновений
# def check_collision(pipes):
#     for pipe in pipes:
#         if bird_rect.colliderect(pipe):
#             return False
#     if bird_rect.top <= -50 or bird_rect.bottom >= HEIGHT:
#         return False
#     return True



class Bird(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((BIRD_WIDTH, BIRD_HEIGHT))
        self.image.fill((255, 255, 0))  # Желтый цвет для птицы
        self.rect = self.image.get_rect(center=(100, HEIGHT // 2))
        self.velocity = 0

    def update(self):
        self.velocity += GRAVITY
        self.rect.y += self.velocity

    def flap(self):
        self.velocity = FLAP_STRENGTH

class Pipe(pygame.sprite.Sprite):
    def __init__(self, x):
        super().__init__()
        self.image = pygame.Surface((PIPE_WIDTH, PIPE_HEIGHT))
        self.image.fill(GREEN)
        height = random.randint(200, 400)
        self.rect = self.image.get_rect(midtop=(500, height))

        # bottom_pipe = pipe_surface.get_rect(midtop=(500, height))
        # top_pipe = pipe_surface.get_rect(midbottom=(500, height - 150))

    def update(self):
        self.rect.x -= 5
        if self.rect.x < -PIPE_WIDTH:
            self.kill()


# Основной игровой цикл
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
pipes = pygame.sprite.Group()
bird = Bird()
all_sprites.add(bird)

# SPAWNPIPE = pygame.USEREVENT
# pygame.time.set_timer(SPAWNPIPE, 1200)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_active:
                bird.flap()
            if event.key == pygame.K_UP and game_active:
                bird.flap()

        # Обработка нажатия мыши для прыжка
        if event.type == pygame.MOUSEBUTTONDOWN and game_active:
            bird.flap()

    all_sprites.update()
    screen.fill(WHITE)
    all_sprites.draw(screen)

    if game_active:
        if pygame.sprite.spritecollide(bird, pipes, False) or bird.rect.top <= -50 or bird.rect.bottom >= HEIGHT:
            game_active = False
            print("f")
        else:
            game_active = True

        # Генерация труб
        if random.randint(1, 500) <= 10:  # Примерный шанс появления трубы
            pipe = Pipe(WIDTH)
            all_sprites.add(pipe)
            pipes.add(pipe)

    else:
        # Вызов функции для отображения сообщения "Игра окончена"
        display_game_over(screen, WIDTH, HEIGHT)

    pygame.display.flip()
    clock.tick(60)

# clock = pygame.time.Clock()
# bird_rect = bird_surface.get_rect(center=(100, HEIGHT // 2))
# SPAWNPIPE = pygame.USEREVENT
# pygame.time.set_timer(SPAWNPIPE, 1200)
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             exit()
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_SPACE and game_active:
#                 bird_movement = 0
#                 bird_movement -= 10
#             if event.key == pygame.K_SPACE and not game_active:
#                 game_active = True
#                 pipes.clear()
#                 bird_rect.center = (100, HEIGHT // 2)
#                 bird_movement = 0
#                 score = 0
#             if event.key == pygame.K_UP and game_active:
#                 bird_movement = 0
#                 bird_movement -= 10
#             if event.key == pygame.K_UP and not game_active:
#                 game_active = True
#                 pipes.clear()
#                 bird_rect.center = (100, HEIGHT // 2)
#                 bird_movement = 0
#                 score = 0
#
#         # Обработка нажатия мыши для прыжка
#         if event.type == pygame.MOUSEBUTTONDOWN and game_active:
#             bird_movement = 0
#             bird_movement -= 10  # Прыжок
#         if event.type == pygame.MOUSEBUTTONDOWN and not game_active:
#             game_active = True
#             pipes.clear()
#             bird_rect.center = (100, HEIGHT // 2)
#             bird_movement = 0
#             score = 0
#
#         if event.type == SPAWNPIPE:
#             pipes.extend(create_pipe())
#
#     screen.fill(WHITE)
#
#     if game_active:
#         # Движение птицы
#         bird_movement += gravity
#         bird_rect.centery += bird_movement
#         game_active = check_collision(pipes)
#
#         # Отображение птицы и труб
#         screen.blit(bird_surface, bird_rect)
#         pipes = move_pipes(pipes)
#         draw_pipes(pipes)
#
#     else:
#         display_game_over(screen, WIDTH, HEIGHT)  # Вызов функции для отображения сообщения "Игра окончена"
#
#     pygame.display.flip()
#     clock.tick(120)
