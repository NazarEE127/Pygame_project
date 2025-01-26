import pygame
#from go_interface import *  # Импортируем функцию из go_interface
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
        self.score = 0

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
            bird.score += 1



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

def menu():
    fon = pygame.transform.scale(load_image('menu_fon.jpg'), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))
    head_font = pygame.font.Font(None, 40)
    text_surface = head_font.render(f"Меню", True, pygame.Color('black'))
    text_rect = text_surface.get_rect(center=(WIDTH // 2, 25))
    main_font = pygame.font.Font(None, 24)

    text_surface2 = main_font.render(f"Бесконечный уровень", True, pygame.Color('black'))
    text_rect2 = text_surface.get_rect(center=(50, 100))
    screen.blit(text_surface, text_rect)
    screen.blit(text_surface2, text_rect2)
    button_surface = pygame.Surface((50, 50))
    button_img = pygame.transform.scale(load_image('button.png'), (50, 50))
    button_surface.blit(button_img, (0, 0))
    button_rect = pygame.Rect(200, 70, 50, 50)
    #pygame.draw.lines(button_surface, (255, 0, 0), True,[[10, 10], [40, 25], [10, 40]], 2)
    screen.blit(button_surface, (button_rect.x, button_rect.y))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if button_rect.collidepoint(event.pos):
                    return # начинаем игру

        pygame.display.flip()
        clock.tick(60)


def start_screen():
    intro_text = ["Flappy Bird",
                  "  by Yandex lyceum", "",
                  'Нажмите "Space"']

    fon = pygame.transform.scale(load_image('start_fon.jpg'), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 50
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('black'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                return  # начинаем игру
        pygame.display.flip()
        clock.tick(60)


def infinit_lvl(game_active):
    fon = pygame.transform.scale(load_image('fon.jpg'), (WIDTH, HEIGHT))

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
                two_pipe = create_pipe()
                pipes.add(two_pipe)

        all_sprites.update()
        screen.blit(fon, (0, 0))
        all_sprites.draw(screen)
        font = pygame.font.Font(None, 50)
        text_surface = font.render(f"Счёт:{bird.score}", True, (255, 0, 0))
        text_rect = text_surface.get_rect(center=(50, 50))
        screen.blit(text_surface, text_rect)

        if game_active:
            if pygame.sprite.spritecollide(bird, pipes, False) or bird.rect.top <= -50 or bird.rect.bottom >= HEIGHT:
                game_active = False
            else:
                game_active = True
            draw_pipes(pipes)

        else:
            return
        pygame.display.flip()
        clock.tick(60)

def display_game_over(screen, width, height):
    screen.fill((255, 255, 255))
    font = pygame.font.Font(None, 74)
    text_surface = font.render("Игра окончена", True, (255, 0, 0))
    text_rect = text_surface.get_rect(center=(width // 2, height // 2))
    screen.blit(text_surface, text_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                pygame.quit()
                exit()
        pygame.display.flip()
        clock.tick(60)




# Основной игровой цикл
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
pipes = pygame.sprite.Group()

bird = Bird()
all_sprites.add(bird)

game_active = True
score = 0


SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE, 1300)

while True:
    start_screen()
    menu()
    infinit_lvl(game_active)
    display_game_over(screen, WIDTH, HEIGHT)
