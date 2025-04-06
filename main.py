import pygame
import random

pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Игра Тир")

# Загрузка изображений
icon = pygame.image.load("img/icon.jpg")
pygame.display.set_icon(icon)
target_img = pygame.image.load("img/target.png")
cursor_img = pygame.image.load("img/cursor.png")

# Получаем размеры изображения цели
target_width = target_img.get_width()
target_height = target_img.get_height()
target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)

# Цвет фона
color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Скрываем стандартный курсор
pygame.mouse.set_visible(False)

running = True
while running:
    screen.fill(color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)

    # Отрисовка цели
    screen.blit(target_img, (target_x, target_y))

    # Отрисовка курсора на месте мыши
    mouse_x, mouse_y = pygame.mouse.get_pos()
    screen.blit(cursor_img, (mouse_x, mouse_y))

    pygame.display.update()

pygame.quit()
