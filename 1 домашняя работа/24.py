import math
import random
x = random.uniform(-10, 10)
print(f"x = {x}")

if x > 0:
    result = 2 * math.sin(x)
else:
    result = x - 6

print(f"f(x) = {result}")
