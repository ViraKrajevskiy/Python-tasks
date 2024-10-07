import random
num = random.randint(100, 999)
result = sorted(str(num)) == list(str(num))
print(result)
