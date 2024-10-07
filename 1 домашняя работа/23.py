import random
A_x = random.randint(0, 10)
A_y = random.randint(0, 10)
B_x = random.randint(0, 10)
B_y = random.randint(0, 10)
C_x = random.randint(0, 10)
C_y = random.randint(0, 10)

print(f"Координаты трёх вершин: A({A_x}, {A_y}), B({B_x}, {B_y}), C({C_x}, {C_y})")

if A_x == B_x:
    D_x = C_x
elif A_x == C_x:
    D_x = B_x
else:
    D_x = A_x

if A_y == B_y:
    D_y = C_y
elif A_y == C_y:
    D_y = B_y
else:
    D_y = A_y

print(f"Координаты четвёртой вершины: D({D_x}, {D_y})")
