
def max_of_non_common_elements(arr1, arr2):

    unique_in_arr1 = set(arr1) - set(arr2)
    unique_in_arr2 = set(arr2) - set(arr1)
    all_unique = unique_in_arr1.union(unique_in_arr2)
    return max(all_unique) if all_unique else None

arr1 = [1, 2, 3, 4]
arr2 = [3, 4, 5, 6]
result = max_of_non_common_elements(arr1, arr2)
print(result)
