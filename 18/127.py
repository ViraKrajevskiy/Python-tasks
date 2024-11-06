def array_127(array, K):
    result = []
    current_series = []
    previous_value = None

    for element in array:
        if element == previous_value:
            current_series.append(element)
        else:
            if len(current_series) > K:
                result.extend([0] * len(current_series))
            else:
                result.extend(current_series)
            current_series = [element]
        previous_value = element

    if len(current_series) > K:
        result.extend([0] * len(current_series))
    else:
        result.extend(current_series)

    return result

array = [1, 1, 2, 2, 2, 3, 3]
print(array_127(array, 2))
