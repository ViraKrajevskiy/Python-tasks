import random
x = random.uniform(-10, 10)
print(f"x = {x}")

if x < -2 or x > 2:
    result = 2 * x
else:
    result = -3 * (x ** 2)

print(f"f(x) = {result}")
