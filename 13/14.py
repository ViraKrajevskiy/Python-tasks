import random
B = 50
n1 = random.randint(1, 100)
n2 = random.randint(1, 100)
n3 = random.randint(1, 100)

max_bounded = None
if n1 <= B:
    max_bounded = n1
if n2 <= B and (max_bounded is None or n2 > max_bounded):
    max_bounded = n2
if n3 <= B and (max_bounded is None or n3 > max_bounded):
    max_bounded = n3

print("Числа:", n1, n2, n3)
print("Максимальное не больше B:", max_bounded)
