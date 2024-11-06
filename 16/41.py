def sum_double_of_evens(arr):
    even_sum = sum(x for x in arr if x % 2 == 0)
    return 2 * even_sum if even_sum > 0 else 0

arr = [2, 3, 4, 6, 7]
print(sum_double_of_evens(arr))