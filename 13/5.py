import random
m1 = random.randint(1, 100)
v1 = random.randint(1, 10)
m2 = random.randint(1, 100)
v2 = random.randint(1, 10)

density1 = m1 / v1
density2 = m2 / v2

max_density = max(density1, density2)

print("Масса и объем 1:", m1, v1, "Плотность:", density1)
print("Масса и объем 2:", m2, v2, "Плотность:", density2)
print("Максимальная плотность:", max_density)
