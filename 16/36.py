def max_non_local_extreme(arr):
    non_extremes = []
    for i in range(1, len(arr) - 1):
        if not (arr[i] < arr[i - 1] and arr[i] < arr[i + 1]) and not (arr[i] > arr[i - 1] and arr[i] > arr[i + 1]):
            non_extremes.append(arr[i])
    return max(non_extremes) if non_extremes else float('-inf')

arr = [7, 3, 8, 1, 6]
print(max_non_local_extreme(arr))