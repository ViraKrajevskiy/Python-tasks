import random
A = random.randint(1, 100)
B = random.randint(1, 100)
C = random.randint(1, 100)
print(f"Числа: A = {A}, B = {B}, C = {C}")

result = sum(sorted([A, B, C])[1:])
print(f"Сумма двух наибольших: {result}")
