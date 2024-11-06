def add_element_to_array(arr, new_element):
    for sub_array in arr:
        sub_array.append(new_element)
    return arr

array = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_element = 10
result = add_element_to_array(array, new_element)
print(result)
