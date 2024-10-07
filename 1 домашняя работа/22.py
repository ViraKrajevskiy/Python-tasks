import _random
import random

x = random.randint(-10, 10)
y = random.randint(-10, 10)

while x == 0 or y == 0:  # Убедимся, что точка не лежит на осях
    x = random.randint(-10, 10)
    y = random.randint(-10, 10)

print(f"Координаты точки: x = {x}, y = {y}")

if x > 0 and y > 0:
    print("Точка находится в первой четверти.")
elif x < 0 and y > 0:
    print("Точка находится во второй четверти.")
elif x < 0 and y < 0:
    print("Точка находится в третьей четверти.")
else:
    print("Точка находится в четвертой четверти.")
