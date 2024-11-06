def find_min_difference_indices(arr):
    min_diff = float('inf')
    index = -1

    for i in range(len(arr) - 1):
        diff = abs(arr[i] - arr[i+1])
        if diff < min_diff:
            min_diff = diff
            index = i

    return index, index+1

arr = [5, 3, 8, 9, 1]
print(find_min_difference_indices(arr))