import random
a1 = random.randint(1, 10)
b1 = random.randint(1, 10)
a2 = random.randint(1, 10)
b2 = random.randint(1, 10)

area1 = a1 * b1
area2 = a2 * b2

max_area = max(area1, area2)

print("Прямоугольник 1:", a1, "x", b1, "Площадь:", area1)
print("Прямоугольник 2:", a2, "x", b2, "Площадь:", area2)
print("Максимальная площадь:", max_area)
