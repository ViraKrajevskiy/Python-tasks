def count_unique_elements(arr):
    unique_elements = set()

    for elem in arr:
        unique_elements.add(elem)

    return len(unique_elements)

arr = [1, 2, 2, 3, 3, 3, 4, 5, 5]
print(count_unique_elements(arr))
