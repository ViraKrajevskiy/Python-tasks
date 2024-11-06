import pygame
import sys

# Инициализация Pygame
pygame.init()

# Установки экрана
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pобеда")

# Цвета
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Класс пули
class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((5, 10))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = (400, 550)  # Позиция пули в нижней части экрана

    def update(self):
        self.rect.y -= 5  # Двигаем пулю вверх
        if self.rect.bottom < 0:
            self.kill()  # Удаляем пулю, если она выходит за экран

# Класс противника
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (400, 100)  # Позиция противника

    def update(self):
        pass

# Создаем группы спрайтов
all_sprites = pygame.sprite.Group()
bullets = pygame.sprite.Group()
enemies = pygame.sprite.Group()

# Создаем пулю и противника
bullet = Bullet()
enemy = Enemy()

# Добавляем спрайты в группы
all_sprites.add(bullet)
all_sprites.add(enemy)
bullets.add(bullet)
enemies.add(enemy)

# Флаг победы
won = False

# Основной игровой цикл
while True:
    screen.fill(WHITE)

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Обновление всех спрайтов
    all_sprites.update()

    # Проверка на столкновение пули и противника
    if pygame.sprite.spritecollideany(bullet, enemies):
        won = True
        bullet.kill()  # Удаляем пулю, если она попала в противника

    # Если победа
    if won:
        font = pygame.font.Font(None, 74)
        text = font.render("Вы победили!", True, (0, 128, 0))
        screen.blit(text, (250, 250))

    # Отображение всех спрайтов
    all_sprites.draw(screen)

    # Обновление экрана
    pygame.display.flip()

    # Устанавливаем частоту кадров
    pygame.time.Clock().tick(60)
