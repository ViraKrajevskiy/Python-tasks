def largest_right_element(arr, R):
    if R >= len(arr) - 1:
        return "Нет элементов справа"
    return max(arr[R:])

arr = [2, 3, 5, 7, 9]
R = 2
print(largest_right_element(arr, R))
