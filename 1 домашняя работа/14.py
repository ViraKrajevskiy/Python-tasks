import random
A = random.randint(1, 100)
B = random.randint(1, 100)
C = random.randint(1, 100)
print(f"Числа: A = {A}, B = {B}, C = {C}")

sorted_nums = sorted([A, B, C])
print(f"По возрастанию: {sorted_nums}")
print(f"По убыванию: {sorted_nums[::-1]}")
