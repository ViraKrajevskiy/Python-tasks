import random
a1 = random.randint(1, 10)
b1 = random.randint(1, 10)
a2 = random.randint(1, 10)
b2 = random.randint(1, 10)

perimeter1 = 2 * (a1 + b1)
perimeter2 = 2 * (a2 + b2)

max_perimeter = max(perimeter1, perimeter2)

print("Прямоугольник 1:", a1, "x", b1, "Периметр:", perimeter1)
print("Прямоугольник 2:", a2, "x", b2, "Периметр:", perimeter2)
print("Максимальный периметр:", max_perimeter)
