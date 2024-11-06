def min_diff_adjacent(arr):
    min_diff = float('inf')
    result = None
    for i in range(len(arr) - 1):
        diff = (arr[i] - arr[i + 1]) if arr[i] > arr[i + 1] else (arr[i + 1] - arr[i])
        if diff < min_diff:
            min_diff = diff
            result = (arr[i], arr[i + 1])
    return result if result else "Массив слишком мал для сравнения"

arr = [5, 8, 2, 4, 7]
print(min_diff_adjacent(arr))
