def array_117(array):
    result = []
    previous_value = None

    for element in array:
        if element != previous_value:
            result.append(0)
        result.append(element)
        previous_value = element

    return result

array = [1, 1, 2, 2, 3]
print(array_117(array))
