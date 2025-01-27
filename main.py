import pygame
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


def load_image(name):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    return pygame.image.load(fullname)


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
        self.image = pygame.transform.scale(load_image("alter_pipe.png"), (PIPE_WIDTH, PIPE_HEIGHT))
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


def draw_pipes(pipes):
    for pipe in pipes:
        screen.blit(pipe.image, pipe.rect.topleft)


def menu():
    fon = pygame.transform.scale(load_image('menu_fon.jpg'), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))
    head_font = pygame.font.Font(None, 40)
    text_surface = head_font.render(f"Меню", True, pygame.Color('black'))
    text_rect = text_surface.get_rect(center=(WIDTH // 2, 25))
    main_font = pygame.font.Font(None, 24)

    text_surface2 = main_font.render(f"Бесконечный уровень", True, pygame.Color('black'))
    text_rect2 = text_surface2.get_rect(center=(WIDTH // 2, 100))

    screen.blit(text_surface, text_rect)
    screen.blit(text_surface2, text_rect2)
    button_surface = pygame.Surface((50, 50))
    button_img = pygame.transform.scale(load_image('button.png'), (50, 50))
    button_surface.blit(button_img, (0, 0))

    button_rect = button_surface.get_rect(center=(200, 70))

    screen.blit(button_surface, button_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if button_rect.collidepoint(event.pos):
                    return

        pygame.display.flip()
        clock.tick(60)


def start_screen():
    intro_text = ["Flappy Bird",
                  "by Yandex lyceum", "",
                  'Нажмите "Space"']

    fon = pygame.transform.scale(load_image('start_fon.jpg'), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 50
    for line in intro_text:
        string_rendered = font.render(line, True, pygame.Color('black'))
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
                return

        pygame.display.flip()
        clock.tick(60)


def infinit_lvl(game_active):
    fon = pygame.transform.scale(load_image('fon.jpg'), (WIDTH, HEIGHT))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN and game_active:
                if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                    bird.flap()

            if event.type == pygame.MOUSEBUTTONDOWN and game_active:
                bird.flap()

            if event.type == SPAWNPIPE:
                create_pipe()

        all_sprites.update()
        screen.blit(fon, (0, 0))
        all_sprites.draw(screen)
        font = pygame.font.Font(None, 50)
        text_surface = font.render(f"Счёт:{bird.score}", True, (255, 0, 0))
        text_rect = text_surface.get_rect(center=(60, 30))
        screen.blit(text_surface, text_rect)

        if game_active:
            if pygame.sprite.spritecollide(bird, pipes, False) or bird.rect.top <= -50 or bird.rect.bottom >= HEIGHT:
                game_active = False

            draw_pipes(pipes)
        else:
            return

        pygame.display.flip()
        clock.tick(60)


def display_game_over(screen):
    screen.fill(WHITE)

    font = pygame.font.Font(None, 74)
    text_surface = font.render("Игра окончена", True, (255, 0, 0))

    text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))

    screen.blit(text_surface, text_rect)

    # Загрузка изображения перезагрузки
    reboot_image = pygame.transform.scale(load_image('reboot.png'), (50, 50))

    reboot_rect = reboot_image.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))

    screen.blit(reboot_image, reboot_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if reboot_rect.collidepoint(event.pos):
                    return True  # Возвращаем True для перезапуска игры

        pygame.display.flip()
        clock.tick(60)


# Основной игровой цикл
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
pipes = pygame.sprite.Group()

bird = Bird()
all_sprites.add(bird)

game_active = True

SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE, 1300)

while True:
    start_screen()
    menu()

    # Игровой цикл
    while game_active:
        infinit_lvl(game_active)

        # Проверка на завершение игры и отображение экрана завершения
        game_active_result = display_game_over(screen)

        # Если игра завершена и возвращаемся в основной цикл для перезапуска игры.
        if game_active_result:
            all_sprites.empty()
            pipes.empty()
            bird.score = 0
            bird.__init__()
            all_sprites.add(bird)