def min_even_indices(arr):
    even_elements = arr[::2]
    return min(even_elements)

arr = [10, 5, 3, 6, 8, 2]
print(min_even_indices(arr))