import random
n1 = random.randint(1, 100)
n2 = random.randint(1, 100)
n3 = random.randint(1, 100)

max_value = max(n1, n2, n3)
min_value = min(n1, n2, n3)

print("Числа:", n1, n2, n3)
print("Последний экстремальный элемент:", min(min_value, max_value))
