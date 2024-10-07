import random
x = random.uniform(-10, 10)
print(f"x = {x}")

if x <= 0:
    result = -x
elif 0 < x < 2:
    result = x ** 2
else:
    result = 4

print(f"f(x) = {result}")
