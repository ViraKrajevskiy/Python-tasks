def count_increasing_decreasing(arr):
    count = 0
    for i in range(1, len(arr) - 1):
        if arr[i - 1] < arr[i] and arr[i] > arr[i + 1]:
            count += 1
    return count if count > 0 else 0

arr = [1, 3, 2, 4, 6, 5]
print(count_increasing_decreasing(arr))