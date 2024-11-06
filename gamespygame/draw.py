import pygame

import pygame

# Инициализация Pygame
pygame.init()

# Настройки окна
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Рисование дерева")
clock = pygame.time.Clock()

# Цвета
BROWN = (139, 69, 19)  # Коричневый цвет для ствола
GREEN = (34, 139, 34)  # Зеленый цвет для кроны
SKY_BLUE = (135, 206, 235)  # Голубой цвет для фона

# Функция рисования дерева
def draw_tree(surface, x, y):
    """
    Рисует дерево на экране.

    :param surface: Экран или поверхность для рисования
    :param x: Координата X для ствола
    :param y: Координата Y для ствола
    """
    # Рисуем ствол
    trunk_width = 40
    trunk_height = 100
    pygame.draw.rect(surface, BROWN, (x, y, trunk_width, trunk_height))

    # Рисуем крону (три круга)
    crown_radius = 60
    pygame.draw.circle(surface, GREEN, (x + trunk_width // 2, y - 20), crown_radius)
    pygame.draw.circle(surface, GREEN, (x - crown_radius // 2, y + 10), crown_radius)
    pygame.draw.circle(surface, GREEN, (x + trunk_width + crown_radius // 2, y + 10), crown_radius)

# Основной игровой цикл
running = True
while running:
    # Очистка экрана
    screen.fill(SKY_BLUE)

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Рисование дерева
    draw_tree(screen, WIDTH // 2 - 20, HEIGHT - 150)

    # Обновление экрана
    pygame.display.flip()

    # Ограничение FPS
    clock.tick(60)

pygame.quit()
