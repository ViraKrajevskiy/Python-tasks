def indices_smaller_than_left(arr):
    indices = [i for i in range(1, len(arr)) if arr[i] < arr[i - 1]]
    return sorted(indices, reverse=True)
arr = [6, 5, 8, 4, 3, 9]
print(indices_smaller_than_left(arr))