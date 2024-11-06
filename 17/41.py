def max_sum_elements(arr):
    arr_sorted = sorted(arr, reverse=True)
    return arr_sorted[0], arr_sorted[1]

arr = [1, 9, 3, 7, 5]
print(max_sum_elements(arr))
