import random
A = random.randint(1, 100)
B = random.randint(1, 100)
C = random.randint(1, 100)
print(f"Числа: A = {A}, B = {B}, C = {C}")

if A < B < C:
    A, B, C = A*2, B*2, C*2
else:
    A, B, C = -A, -B, -C

print(f"Результат: A = {A}, B = {B}, C = {C}")
