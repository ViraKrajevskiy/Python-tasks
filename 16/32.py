def first_local_minimum(arr):
    for i in range(1, len(arr) - 1):
        if arr[i] < arr[i - 1] and arr[i] < arr[i + 1]:
            return arr[i]
    return float('inf')
arr = [5, 3, 8, 2, 9]
print(first_local_minimum(arr))