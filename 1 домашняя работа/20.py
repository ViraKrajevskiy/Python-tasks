import random
A = random.randint(1, 100)
B = random.randint(1, 100)
C = random.randint(1, 100)
print(f"Точки: A = {A}, B = {B}, C = {C}")

dist_AB = abs(A - B)
dist_AC = abs(A - C)
dist_BC = abs(B - C)

min_distance = min(dist_AB, dist_AC, dist_BC)
print(f"Минимальное расстояние: {min_distance}")
