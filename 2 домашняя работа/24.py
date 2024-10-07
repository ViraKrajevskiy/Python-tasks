import random
import math

a, b, c = random.randint(1, 10), random.randint(-10, 10), random.randint(-10, 10)
D = b**2 - 4*a*c
result = D >= 0
print(result)
