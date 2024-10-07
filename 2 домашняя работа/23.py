import random
num = random.randint(100, 999)
result = str(num) == str(num)[::-1]
print(result)


