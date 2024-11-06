def closest_two_by_index_v2(arr, R):
    if R < 1:
        return arr[1]
    elif R > len(arr) - 2:
        return arr[-2]
    else:
        return arr[R - 1], arr[R + 1]

arr = [1, 4, 7, 9, 11]
R = 2
print(closest_two_by_index_v2(arr, R))
