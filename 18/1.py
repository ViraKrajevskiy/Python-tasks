def sum_of_common_elements(arr1, arr2):

    common_elements = set(arr1).intersection(set(arr2))
    return sum(common_elements)

arr1 = [1, 2, 3, 4]
arr2 = [3, 4, 5, 6]
result = sum_of_common_elements(arr1, arr2)
print(result)
