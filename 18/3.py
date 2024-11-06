def sum_of_non_common_elements(arr1, arr2):

    unique_in_arr1 = set(arr1) - set(arr2)
    unique_in_arr2 = set(arr2) - set(arr1)
    return sum(unique_in_arr1) + sum(unique_in_arr2)

arr1 = [1, 2, 3, 4]
arr2 = [3, 4, 5, 6]
result = sum_of_non_common_elements(arr1, arr2)
print(result)
