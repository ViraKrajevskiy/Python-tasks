def create_array_b(a):
    b = []
    for k in range(len(a)):
        b.append(a[0] + k)
    return b

a = [5, 6, 7]
b = create_array_b(a)
print(b)