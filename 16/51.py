def swap_arrays(a, b):

    a, b = b, a
    return a, b

a = [1, 2, 3]
b = [4, 5, 6]
a, b = swap_arrays(a, b)
print("Массив a:", a)  # Выведет: [4, 5, 6]
print("Массив b:", b)  # Выведет: [1, 2, 3]
