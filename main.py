import pygame
from go_interface import display_game_over  # Импортируем функцию из go_interface
import random
import os
import sys

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


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


class Bird(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(load_image("bird.png"), (BIRD_WIDTH, BIRD_HEIGHT))
        self.rect = self.image.get_rect(center=(100, HEIGHT // 2))
        self.velocity = 0

    def update(self):
        self.velocity += GRAVITY
        self.rect.y += self.velocity

    def flap(self):
        self.velocity = FLAP_STRENGTH


class Down_pipe(pygame.sprite.Sprite):
    def __init__(self, h):
        super().__init__()
        self.image = pygame.transform.scale(load_image("pipe.png"), (PIPE_WIDTH, PIPE_HEIGHT))
        self.rect = self.image.get_rect(midtop=(500, h))

    def update(self):
        self.rect.x -= 5
        if self.rect.x < -PIPE_WIDTH:
            self.kill()


class Up_pipe(pygame.sprite.Sprite):
    def __init__(self, h):
        super().__init__()
        self.image = pygame.transform.scale(load_image("pipe.png"), (PIPE_WIDTH, PIPE_HEIGHT))
        self.rect = self.image.get_rect(midbottom=(500, h - 150))

    def update(self):
        self.rect.x -= 5
        if self.rect.x < -PIPE_WIDTH:
            self.kill()


# Создание труб
def create_pipe():
    height = random.randint(100, 450)
    bottom_pipe = Down_pipe(height)
    top_pipe = Up_pipe(height)
    all_sprites.add(bottom_pipe)
    pipes.add(bottom_pipe)
    all_sprites.add(top_pipe)
    pipes.add(top_pipe)
    return bottom_pipe, top_pipe


# Отображение труб на экране
def draw_pipes(pipes):
    for pipe in pipes:
        if pipe.rect.bottom >= HEIGHT:
            pipes.draw(screen)
        else:
            flipped_pipe = pygame.transform.flip(screen, False, True)
            pipes.draw(flipped_pipe)


# Основной игровой цикл
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
pipes = pygame.sprite.Group()

bird = Bird()
all_sprites.add(bird)


SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE, 1300)


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

        if event.type == SPAWNPIPE:
            pipes.add(create_pipe())

    all_sprites.update()
    screen.fill(WHITE)
    all_sprites.draw(screen)

    if game_active:
        if pygame.sprite.spritecollide(bird, pipes, False) or bird.rect.top <= -50 or bird.rect.bottom >= HEIGHT:
            game_active = False
        else:
            game_active = True
        draw_pipes(pipes)

    else:
        # Вызов функции для отображения сообщения "Игра окончена"
        display_game_over(screen, WIDTH, HEIGHT)

    pygame.display.flip()
    clock.tick(60)
