import pygame
pygame.init()

# Настройка окна
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Ввод текста от пользователя")

# Цвета и шрифт
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
font = pygame.font.Font(None, 36)

# Переменная для хранения текста
input_text = ""
running = True

while running:
    # Очистка экрана
    screen.fill(WHITE)

    for event in pygame.event.get():
        # Если пользователь закрыл окно
        if event.type == pygame.QUIT:
            running = False

        # Если пользователь нажал клавишу
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:  # Нажатие Enter
                print(f"Введенный текст: {input_text}")
                input_text = ""  # Очистить поле после подтверждения
            elif event.key == pygame.K_BACKSPACE:  # Удаление символа
                input_text = input_text[:-1]
            else:  # Добавление символа в строку
                input_text += event.unicode

    # Рендеринг текста
    text_surface = font.render(input_text, True, BLACK)
    screen.blit(text_surface, (20, 20))

    # Обновление экрана
    pygame.display.flip()

pygame.quit()
