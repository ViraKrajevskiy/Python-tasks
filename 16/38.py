def count_decreasing_subarrays(arr):
    count = 0
    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            count += 1
    return count if count > 0 else 0

arr = [5, 4, 6, 3, 2]
print(count_decreasing_subarrays(arr))