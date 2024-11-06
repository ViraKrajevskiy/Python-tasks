def max_among_local_min(arr):
    local_mins = []
    for i in range(1, len(arr) - 1):
        if arr[i] < arr[i - 1] and arr[i] < arr[i + 1]:
            local_mins.append(arr[i])
    return max(local_mins) if local_mins else float('-inf')

arr = [10, 2, 9, 4, 1, 6]
print(max_among_local_min(arr))