import random

a, b, c = random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)
result = a == b or b == c or a == c
print(result)
