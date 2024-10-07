import random
x1, y1 = random.randint(1, 8), random.randint(1, 8)
x2, y2 = random.randint(1, 8), random.randint(1, 8)
result = (x1 + y1) % 2 == (x2 + y2) % 2
print(result)
