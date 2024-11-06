def count_repeated_elements(arr):
    element_count = {}

    for elem in arr:
        element_count[elem] = element_count.get(elem, 0) + 1

    repeated_count = sum(1 for count in element_count.values() if count > 1)

    return repeated_count

arr = [1, 2, 2, 3, 3, 4, 5]
print(count_repeated_elements(arr))