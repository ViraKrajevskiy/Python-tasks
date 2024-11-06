def find_duplicate_index(arr):

    element_indices = {}

    for i, elem in enumerate(arr):
        if elem in element_indices:
            return element_indices[elem]
        else:
            element_indices[elem] = i

    return -1

arr = [3, 1, 4, 2, 5, 4]
print(find_duplicate_index(arr))