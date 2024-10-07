import random
A = random.randint(1, 100)
B = random.randint(1, 100)
C = random.randint(1, 100)
print(f"Числа: A = {A}, B = {B}, C = {C}")

result = (max(A, B, C) + min(A, B, C)) / 2
print(f"Среднее между максимальным и минимальным: {result}")
