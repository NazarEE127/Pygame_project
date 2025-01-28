import pygame
import random
import os
import sys

# Инициализация Pygame
pygame.init()

# Настройки экрана
WIDTH, HEIGHT = 450, 600
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

    button_surface = pygame.Surface((50, 50))
    button_img = pygame.transform.scale(load_image('button.png'), (50, 50))
    button_surface.blit(button_img, (0, 0))
    button_rect = button_surface.get_rect(center=(200, 70))

    text_surface3 = main_font.render(f"1-й уровень", True, pygame.Color('black'))
    text_rect3 = text_surface3.get_rect(center=(WIDTH // 2, 200))

    button_surface2 = pygame.Surface((50, 50))
    button_surface2.blit(button_img, (0, 0))

    button_rect2 = button_surface2.get_rect(center=(200, 160))

    text_surface4 = main_font.render(f"2-й уровень", True, pygame.Color('black'))
    text_rect4 = text_surface3.get_rect(center=(WIDTH // 2, 300))

    button_surface3 = pygame.Surface((50, 50))
    button_surface3.blit(button_img, (0, 0))

    button_rect3 = button_surface3.get_rect(center=(200, 250))

    screen.blit(text_surface, text_rect)
    screen.blit(text_surface2, text_rect2)
    screen.blit(text_surface3, text_rect3)
    screen.blit(text_surface4, text_rect4)
    screen.blit(button_surface, button_rect)
    screen.blit(button_surface2, button_rect2)
    screen.blit(button_surface3, button_rect3)

    text_surface_change_skin = head_font.render(f"Выбор скина", True, pygame.Color('black'))
    text_rect_change_skin = text_surface_change_skin.get_rect(center=(WIDTH // 2, 350))
    screen.blit(text_surface_change_skin, text_rect_change_skin)

    bird = Bird()
    all_sprites.add(bird)

    cur_skin_surface = pygame.Surface((BIRD_WIDTH, BIRD_HEIGHT))
    cur_skin = bird.image
    cur_skin_surface.blit(cur_skin, (0, 0))
    cur_skin_rect = cur_skin_surface.get_rect(center=(WIDTH // 2 + 120, 350))
    screen.blit(cur_skin_surface, cur_skin_rect)

    skin_surface = pygame.Surface((BIRD_WIDTH*2, BIRD_HEIGHT*2))
    skin1 = pygame.transform.scale(load_image("bird.png"), (BIRD_WIDTH*2, BIRD_HEIGHT*2))
    skin_surface.blit(skin1, (0, 0))
    skin1_rect = skin_surface.get_rect(center=(50, 400))
    screen.blit(skin_surface, skin1_rect)

    skin2_surface = pygame.Surface((BIRD_WIDTH * 2, BIRD_HEIGHT * 2))
    skin2 = pygame.transform.scale(load_image("bird2.png"), (BIRD_WIDTH * 2, BIRD_HEIGHT * 2))
    skin2_surface.blit(skin2, (0, 0))
    skin2_rect = skin2_surface.get_rect(center=(140, 400))
    screen.blit(skin2_surface, skin2_rect)

    skin3_surface = pygame.Surface((BIRD_WIDTH * 2, BIRD_HEIGHT * 2))
    skin3 = pygame.transform.scale(load_image("bird3.png"), (BIRD_WIDTH * 2, BIRD_HEIGHT * 2))
    skin3_surface.blit(skin3, (0, 0))
    skin3_rect = skin3_surface.get_rect(center=(230, 400))
    screen.blit(skin3_surface, skin3_rect)

    skin4_surface = pygame.Surface((BIRD_WIDTH * 2, BIRD_HEIGHT * 2))
    skin4 = pygame.transform.scale(load_image("bird4.png"), (BIRD_WIDTH * 2, BIRD_HEIGHT * 2))
    skin4_surface.blit(skin4, (0, 0))
    skin4_rect = skin4_surface.get_rect(center=(320, 400))
    screen.blit(skin4_surface, skin4_rect)

    skin5_surface = pygame.Surface((BIRD_WIDTH * 2, BIRD_HEIGHT * 2))
    skin5 = pygame.transform.scale(load_image("bird5.png"), (BIRD_WIDTH * 2, BIRD_HEIGHT * 2))
    skin5_surface.blit(skin5, (0, 0))
    skin5_rect = skin5_surface.get_rect(center=(410, 400))
    screen.blit(skin5_surface, skin5_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if button_rect.collidepoint(event.pos):
                    return bird
                if button_rect2.collidepoint(event.pos):
                    print(1)
                if button_rect3.collidepoint(event.pos):
                    print(2)

                if skin1_rect.collidepoint(event.pos):
                    cur_skin = pygame.transform.scale(load_image("bird.png"), (BIRD_WIDTH, BIRD_HEIGHT))
                    bird.image = pygame.transform.scale(load_image("bird.png"), (BIRD_WIDTH, BIRD_HEIGHT))

                if skin2_rect.collidepoint(event.pos):
                    cur_skin = pygame.transform.scale(load_image("bird2.png"), (BIRD_WIDTH, BIRD_HEIGHT))
                    bird.image = pygame.transform.scale(load_image("bird2.png"), (BIRD_WIDTH, BIRD_HEIGHT))

                if skin3_rect.collidepoint(event.pos):
                    cur_skin = pygame.transform.scale(load_image("bird3.png"), (BIRD_WIDTH, BIRD_HEIGHT))
                    bird.image = pygame.transform.scale(load_image("bird3.png"), (BIRD_WIDTH, BIRD_HEIGHT))

                if skin4_rect.collidepoint(event.pos):
                    cur_skin = pygame.transform.scale(load_image("bird4.png"), (BIRD_WIDTH, BIRD_HEIGHT))
                    bird.image = pygame.transform.scale(load_image("bird4.png"), (BIRD_WIDTH, BIRD_HEIGHT))

                if skin5_rect.collidepoint(event.pos):
                    cur_skin = pygame.transform.scale(load_image("bird5.png"), (BIRD_WIDTH, BIRD_HEIGHT))
                    bird.image = pygame.transform.scale(load_image("bird5.png"), (BIRD_WIDTH, BIRD_HEIGHT))

                cur_skin_surface.blit(cur_skin, (0, 0))
                cur_skin_rect = cur_skin_surface.get_rect(center=(WIDTH // 2 + 120, 350))
                screen.blit(cur_skin_surface, cur_skin_rect)

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


def infinit_lvl(game_active, bird):
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


def display_game_over(screen, score):
    screen.fill(WHITE)

    font = pygame.font.Font(None, 74)
    text_surface = font.render("Игра окончена", True, (255, 0, 0))

    text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 200))

    text_score_surface = font.render(f"Ваш счёт: {score}", True, (255, 0, 0))

    text_score_rect = text_score_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 100))

    screen.blit(text_surface, text_rect)
    screen.blit(text_score_surface, text_score_rect)

    # Загрузка изображения перезагрузки
    reboot_image = pygame.transform.scale(load_image('reboot.png'), (50, 50))

    reboot_rect = reboot_image.get_rect(center=(WIDTH // 2 - 50, HEIGHT // 2 + 50))

    menu_image = pygame.transform.scale(load_image('menu.png'), (50, 50))

    menu_rect = reboot_image.get_rect(center=(WIDTH // 2 + 50, HEIGHT // 2 + 50))

    screen.blit(reboot_image, reboot_rect)
    screen.blit(menu_image, menu_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if reboot_rect.collidepoint(event.pos):
                    return True  # Возвращаем True для перезапуска игры
                if menu_rect.collidepoint(event.pos):
                    return False

        pygame.display.flip()
        clock.tick(60)


# Основной игровой цикл
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
pipes = pygame.sprite.Group()


game_active = True
menu_active = False
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE, 1300)

while True:
    if menu_active is False:
        start_screen()

    bird = menu()

    # Игровой цикл
    while game_active:
        infinit_lvl(game_active, bird)

        # Проверка на завершение игры и отображение экрана завершения
        game_active_result = display_game_over(screen, bird.score)
        if game_active_result is False:
            menu_active = True
            all_sprites.empty()
            pipes.empty()
            break

        # Если игра завершена и возвращаемся в основной цикл для перезапуска игры.
        if game_active_result:
            all_sprites.empty()
            pipes.empty()
            bird.score = 0
            bird.rect = bird.image.get_rect(center=(100, HEIGHT // 2))
            bird.velocity = 0
            all_sprites.add(bird)


