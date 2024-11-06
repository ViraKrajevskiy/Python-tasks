def create_b_from_even_indices(a):
    b = [a[i] for i in range(0, len(a), 2)]
    return b

a = [1, 2, 3, 4, 5, 6]
b = create_b_from_even_indices(a)
print(b)
