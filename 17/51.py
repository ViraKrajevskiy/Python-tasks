def common_elements(arr1, arr2):
    common = list(set(arr1) & set(arr2))
    return common if common else "Нет общих элементов"

arr1 = [1, 2, 3, 4]
arr2 = [3, 4, 5, 6]
print(common_elements(arr1, arr2))
