def closest_two_by_index(arr, R):
    if R in arr:
        R_index = arr.index(R)
        if R_index == 0:
            return arr[R_index + 1]
        elif R_index == len(arr) - 1:
            return arr[R_index - 1]
        else:
            return arr[R_index - 1], arr[R_index + 1]
    return "Элемента нет в массиве"

arr = [1, 5, 9, 4, 8]
R = 9
print(closest_two_by_index(arr, R))
