def array_124(array, K):
    result = []
    current_series = []
    previous_value = None

    for element in array:
        if element == previous_value:
            current_series.append(element)
        else:
            if current_series and len(current_series) > K:
                result.append(K)
            else:
                result.extend(current_series)
            current_series = [element]
        previous_value = element

    if current_series and len(current_series) > K:
        result.append(K)
    else:
        result.extend(current_series)

    return result

array = [1, 1, 2, 2, 2, 3]
print(array_124(array, 2))
