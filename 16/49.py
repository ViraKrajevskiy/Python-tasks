def find_out_of_range_index(arr):
    n = len(arr)

    for i, elem in enumerate(arr):
        if elem < 1 or elem > n:
            return i

    return -1
arr = [1, 2, 3, 5, 8]

print(find_out_of_range_index(arr))