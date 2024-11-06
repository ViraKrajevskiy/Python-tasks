import random
n1 = random.randint(-100, 100)
n2 = random.randint(-100, 100)
n3 = random.randint(-100, 100)

min_positive = None
if n1 > 0:
    min_positive = n1
if n2 > 0 and (min_positive is None or n2 < min_positive):
    min_positive = n2
if n3 > 0 and (min_positive is None or n3 < min_positive):
    min_positive = n3

print("Числа:", n1, n2, n3)
print("Минимальное положительное:", min_positive)
