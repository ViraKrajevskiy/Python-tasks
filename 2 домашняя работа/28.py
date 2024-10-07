import random
x, y = random.randint(-10, 10), random.randint(-10, 10)
result = (x > 0 and y > 0) or (x < 0 and y < 0)
print(result)
