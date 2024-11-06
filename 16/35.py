def min_among_local_max(arr):
    local_maxs = []
    for i in range(1, len(arr) - 1):
        if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
            local_maxs.append(arr[i])
    return min(local_maxs) if local_maxs else float('inf')

arr = [1, 5, 2, 8, 3, 6]
print(min_among_local_max(arr))