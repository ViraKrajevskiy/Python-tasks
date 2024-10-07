import random
num = random.randint(100, 999)
result = sorted(str(num)) == list(str(num)) or sorted(str(num), reverse=True) == list(str(num))
print(result)
