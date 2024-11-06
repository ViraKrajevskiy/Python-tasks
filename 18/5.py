def is_subset(arr1, arr2):

    return set(arr1).issubset(set(arr2))

arr1 = [1, 2, 3]
arr2 = [1, 2, 3, 4, 5]
result = is_subset(arr1, arr2)
print(result)
