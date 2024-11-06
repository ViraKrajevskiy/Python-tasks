def count_and_max_of_first_list(arr1):

    positive_elements = [x for x in arr1 if x > 0]
    count = len(positive_elements)

    maximum = max(positive_elements) if positive_elements else None
    return count, maximum

arr1 = [1, 2, 3, -1, -2]
result = count_and_max_of_first_list(arr1)
print("Количество:", result[0], "Максимальный элемент:", result[1])
