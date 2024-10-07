import random

A = random.randint(1, 100)
B = random.randint(1, 100)
print(f"Исходные числа: A = {A}, B = {B}")

if A != B:
    if A > B:
        A = A + B
    else:
        B = A + B
else:
    A, B = 0, 0

print(f"Результат: A = {A}, B = {B}")
