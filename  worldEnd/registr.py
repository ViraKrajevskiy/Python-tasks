import pygame

pygame.init()

# Настройки экрана
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Регистрация пользователя")

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Шрифт
font = pygame.font.Font(None, 36)

# Поля ввода
username = ""
password = ""
focus = "username"  # Активное поле
message = ""

# Кнопка "Зарегистрироваться"
button_rect = pygame.Rect(300, 400, 200, 50)

running = True
while running:
    screen.fill(WHITE)  # Очистка экрана

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Обработка ввода текста
        elif event.type == pygame.KEYDOWN:
            if focus == "username":
                if event.key == pygame.K_RETURN:
                    focus = "password"
                elif event.key == pygame.K_BACKSPACE:
                    username = username[:-1]
                else:
                    username += event.unicode

            elif focus == "password":
                if event.key == pygame.K_RETURN:
                    focus = "submit"
                elif event.key == pygame.K_BACKSPACE:
                    password = password[:-1]
                else:
                    password += event.unicode

        # Обработка кликов мыши
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                if username and password:
                    message = f"Пользователь {username} успешно зарегистрирован!"
                    username = ""
                    password = ""
                else:
                    message = "Поля не должны быть пустыми!"

    # Отображение интерфейса
    username_label = font.render("Имя пользователя:", True, BLACK)
    password_label = font.render("Пароль:", True, BLACK)
    message_label = font.render(message, True, GREEN if "успешно" in message else RED)

    screen.blit(username_label, (50, 150))
    screen.blit(password_label, (50, 250))
    screen.blit(message_label, (50, 500))

    # Поля для ввода
    pygame.draw.rect(screen, GRAY if focus == "username" else WHITE, (300, 150, 400, 40))
    pygame.draw.rect(screen, GRAY if focus == "password" else WHITE, (300, 250, 400, 40))

    username_text = font.render(username, True, BLACK)
    password_text = font.render("*" * len(password), True, BLACK)  # Пароль скрыт

    screen.blit(username_text, (310, 160))
    screen.blit(password_text, (310, 260))

    # Кнопка "Зарегистрироваться"
    pygame.draw.rect(screen, GREEN, button_rect)
    button_text = font.render("Зарегистрироваться", True, WHITE)
    screen.blit(button_text, (button_rect.x + 10, button_rect.y + 10))

    pygame.display.flip()

pygame.quit()
