import random
k = 2
n1 = random.randint(1, 100)
n2 = random.randint(1, 100)
n3 = random.randint(1, 100)

min_value = min(n1, n2, n3)
max_value = max(n1, n2, n3)

count = 0
for i in range(min_value, max_value + 1):
    if i % k == 0:
        count += 1

print("Числа:", n1, n2, n3)
print("Количество чисел кратных", k, "между", min_value, "и", max_value, ":", count)
