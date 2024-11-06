def create_array_from_odd_indices(a):
    b = [a[i] for i in range(1, len(a), 2)]
    return b

a = [10, 20, 30, 40, 50, 60]
b = create_array_from_odd_indices(a)
print(b)