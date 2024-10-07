import random
A = random.randint(1, 10)
B = random.randint(1, 10)
C = random.randint(1, 10)
print(f"Числа: A = {A}, B = {B}, C = {C}")

if A == B:
    print("Номер отличающегося числа: 3")
elif A == C:
    print("Номер отличающегося числа: 2")
elif B == C:
    print("Номер отличающегося числа: 1")
else:
    print("Все числа разные")
