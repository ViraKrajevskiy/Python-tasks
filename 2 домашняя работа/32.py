import random
import math

a, b, c = random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)
sides = sorted([a, b, c])
result = math.isclose(sides[0]**2 + sides[1]**2, sides[2]**2)
print(result)