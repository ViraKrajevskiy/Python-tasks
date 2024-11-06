def max_odd_indices(arr):
    odd_elements = arr[1::2]
    return max(odd_elements)

arr = [10, 5, 3, 6, 8, 2]
print(max_odd_indices(arr))