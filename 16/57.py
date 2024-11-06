def create_array_b(a):
    b = []
    for i in range(0, len(a), 2):
        b.append(a[i])
    for i in range(1, len(a), 2):
        b.append(a[i])
    return b

a = [1, 2, 3, 4, 5, 6]
b = create_array_b(a)
print(b)