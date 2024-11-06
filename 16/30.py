def indices_greater_than_left(arr):
    indices = [i for i in range(1, len(arr)) if arr[i] > arr[i - 1]]
    return indices
arr = [1, 3, 2, 5, 4, 6]
print(indices_greater_than_left(arr))