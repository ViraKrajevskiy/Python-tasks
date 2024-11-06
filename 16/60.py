
def create_array_b(a):
    n = len(a)
    b = []
    for k in range(n):
        b.append(sum(a[k:n]))
    return b

a = [1, 2, 3]
b = create_array_b(a)
print(b)