import random

num = random.randint(100, 999)
result = len(set(str(num))) == 3
print(result)
