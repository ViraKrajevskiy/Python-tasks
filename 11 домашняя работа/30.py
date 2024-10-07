import math

A = float(input("Введите значение A: "))
B = float(input("Введите значение B: "))
n = int(input("Введите значение n: "))

step = (B - A) / n
x_values = [A + i * step for i in range(n + 1)]
f_values = [1 - math.sin(x) for x in x_values]

for i, f in enumerate(f_values):
    print(f"F(x[{i}]) = {f}")
