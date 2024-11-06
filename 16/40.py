def count_below_average(arr):
    average = sum(arr) / len(arr)
    count = len([x for x in arr if x < average])
    return count if count > 0 else 0
arr = [10, 2, 3, 8, 6]
print(count_below_average(arr))