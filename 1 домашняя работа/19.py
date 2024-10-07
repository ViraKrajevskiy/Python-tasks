import random
A = random.randint(1, 10)
B = random.randint(1, 10)
C = random.randint(1, 10)
D = random.randint(1, 10)
print(f"Числа: A = {A}, B = {B}, C = {C}, D = {D}")

nums = [A, B, C, D]
for i, num in enumerate(nums):
    if nums.count(num) == 1:
        print(f"Номер отличающегося числа: {i + 1}")
        break
