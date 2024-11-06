def find_unique_elements(arr):
    element_count = {}

    for elem in arr:
        element_count[elem] = element_count.get(elem, 0) + 1

    unique_elements = [elem for elem, count in element_count.items() if count == 1]

    return unique_elements

arr = [7, 4, 2, 3, 1, 5, 2, 7]
print(find_unique_elements(arr))