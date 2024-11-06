def find_elements_diff_two(arr):
    for i in arr:
        for j in arr:
            if (i - j) == 2 or (j - i) == 2:
                return i, j
    return "Нет элементов с разницей 2"

arr = [3, 5, 7, 9, 11]
print(find_elements_diff_two(arr))
