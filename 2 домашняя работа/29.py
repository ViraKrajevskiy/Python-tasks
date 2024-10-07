import random
x, y = random.randint(0, 10), random.randint(0, 10)
x1, y1, x2, y2 = 0, 0, 10, 10
result = x1 < x < x2 and y1 < y < y2
print(result)
