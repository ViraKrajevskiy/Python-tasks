import pygame
import random

# Инициализация Pygame
pygame.init()

# Настройки окна
WIDTH, HEIGHT = 1000, 900
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Привязка пули к игроку")
clock = pygame.time.Clock()

# Класс игрока
class Player:
    def __init__(self, x, y):
        self.pos = pygame.Vector2(x, y)
        self.width = 50
        self.height = 50
        self.speed = 300  # пикселей в секунду

    def draw(self, screen):
        pygame.draw.rect(screen, "blue", (self.pos.x, self.pos.y, self.width, self.height))

    def move(self, keys, dt):
        if keys[pygame.K_w] and self.pos.y > 0:
            self.pos.y -= self.speed * dt
        if keys[pygame.K_s] and self.pos.y < HEIGHT - self.height:
            self.pos.y += self.speed * dt
        if keys[pygame.K_a] and self.pos.x > 0:
            self.pos.x -= self.speed * dt
        if keys[pygame.K_d] and self.pos.x < WIDTH - self.width:
            self.pos.x += self.speed * dt

# Класс врага
class Enemy:
    def __init__(self, x, y):
        self.pos = pygame.Vector2(x, y)
        self.width = 10
        self.height = 10
        self.color = "green"
        self.speed = 300  # Скорость движения врага
        self.direction = 1  # Направление движения: 1 - вправо, -1 - влево

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.pos.x, self.pos.y, self.width, self.height))

    def move(self, dt):
        self.pos.x += self.speed * self.direction * dt
        # Изменение направления при достижении границ
        if self.pos.x <= 0 or self.pos.x >= WIDTH - self.width :
            self.direction *= -1


# Класс пули
class Bullet:
    def __init__(self, x, y):
        self.pos = pygame.Vector2(x, y)
        self.width = 10
        self.height = 10
        self.color = "red"
        self.speed = 500  # Скорость полета

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.pos.x, self.pos.y, self.width, self.height))

    def update(self, dt):
        self.pos.y -= self.speed * dt

# Основной игровой цикл
running = True
player = Player(WIDTH // 2, HEIGHT - 100)
enemies = [Enemy(random.randint(0, WIDTH - 50), random.randint(50, 300)) for _ in range(3)]  # Создаем 3 врагов
bullets = []  # Список для пуль

while running:
    dt = clock.tick(60) / 1000  # Дельта времени
    screen.fill("black")  # Очистка экрана

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Создаем новую пулю на позиции игрока
                bullets.append(Bullet(player.pos.x + player.width // 2 - 5, player.pos.y - 10))

    # Управление игроком
    keys = pygame.key.get_pressed()
    player.move(keys, dt)

    # Обновление пуль
    for bullet in bullets[:]:  # Копируем список для безопасного удаления
        bullet.update(dt)
        # Удаляем пулю, если она вышла за пределы экрана
        if bullet.pos.y < 0:
            bullets.remove(bullet)

    # Обновление врагов
    for enemy in enemies:
        enemy.move(dt)

    # Отрисовка объектов
    player.draw(screen)
    for enemy in enemies:
        enemy.draw(screen)
    for bullet in bullets:
        bullet.draw(screen)

    pygame.display.flip()  # Обновление экрана

pygame.quit()
