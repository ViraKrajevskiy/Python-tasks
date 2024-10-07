import random
x = random.randint(-10, 10)
y = random.randint(-10, 10)
print(f"Координаты точки: x = {x}, y = {y}")

if x == 0 and y == 0:
    print("Точка находится в начале координат")
elif x == 0:
    print("Точка на оси OY")
elif y == 0:
    print("Точка на оси OX")
else:
    print("Точка находится вне осей")
