import random
x = random.uniform(-10, 10)
print(f"x = {x}")

if x < 0:
    result = 0
elif 0 <= x < 1 or 2 <= x < 3 or 4 <= x:
    result = 1
elif 1 <= x < 2 or 3 <= x < 4:
    result = -1

print(f"f(x) = {result}")
