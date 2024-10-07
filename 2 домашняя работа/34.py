import random

a, b, c = random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)
result = a + b > c and a + c > b and b + c > a
print(result)
