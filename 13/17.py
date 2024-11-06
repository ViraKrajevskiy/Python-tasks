import random
import random

N = 10  # количество случайных чисел
max_value = None
last_max_index = -1
count_after_max = 0

for i in range(N):
    current_number = random.randint(1, 100)  # Генерация случайного числа
    print(current_number, end=" ")  # Вывод числа

    # Проверка, является ли текущее число максимальным
    if max_value is None or current_number > max_value:
        max_value = current_number
        last_max_index = i
    elif current_number == max_value:
        last_max_index = i

# Подсчет количества элементов после последнего максимального элемента
count_after_max = N - last_max_index - 1

print("\nМаксимальное значение:", max_value)
print("Количество элементов после последнего максимума:", count_after_max)
