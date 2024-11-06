def array_118(array):
    result = []
    current_series = []
    previous_value = None

    for element in array:
        if element == previous_value:
            current_series.append(element)
        else:
            if current_series:
                result.extend(current_series)
                result.append(0)
            current_series = [element]
        previous_value = element

    if current_series:
        result.extend(current_series)
        result.append(0)

    return result

array = [1, 1, 2, 2, 3]
print(array_118(array))
