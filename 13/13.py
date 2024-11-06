import random
n1 = random.randint(1, 100)
n2 = random.randint(1, 100)
n3 = random.randint(1, 100)



max_odd = None
if n1 % 2 != 0:
    max_odd = n1
if n2 % 2 != 0 and (max_odd is None or n2 > max_odd):
    max_odd = n2
if n3 % 2 != 0 and (max_odd is None or n3 > max_odd):
    max_odd = n3

print("Числа:", n1, n2, n3)
print("Максимальное нечетное:", max_odd)
