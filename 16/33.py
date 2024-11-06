def last_local_maximum(arr):
    for i in range(len(arr) - 2, 0, -1):
        if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
            return arr[i]
    return float('-inf')

arr = [1, 4, 3, 6, 5]
print(last_local_maximum(arr))