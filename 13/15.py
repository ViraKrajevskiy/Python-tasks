import random
n1 = random.randint(1, 100)
n2 = random.randint(1, 100)
n3 = random.randint(1, 100)

max1 = max(n1, n2, n3)
max2 = min(n1, n2, n3)

if n1 != max1 and n1 > max2:
    max2 = n1
if n2 != max1 and n2 > max2:
    max2 = n2
if n3 != max1 and n3 > max2:
    max2 = n3

print("Числа:", n1, n2, n3)
print("Два наибольших:", max1, max2)
