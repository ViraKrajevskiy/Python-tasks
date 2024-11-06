def array_121(array):
    result = []
    previous_value = None

    for element in array:
        if element == previous_value:
            result.extend([element, element])
        else:
            result.append(element)
            result.append(element)
        previous_value = element

    return result

array = [1, 1, 2, 2, 3]
print(array_121(array))
