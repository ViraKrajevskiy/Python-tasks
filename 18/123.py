def array_123(array, K):
    result = []
    current_series = []
    previous_value = None
    replaced = False

    for element in array:
        if element == previous_value:
            current_series.append(element)
        else:
            if len(current_series) > K and not replaced:
                result.append(K)  # Замена на K
                replaced = True
            else:
                result.extend(current_series)
            current_series = [element]
        previous_value = element

    if len(current_series) > K and not replaced:
        result.append(K)
    else:
        result.extend(current_series)

    return result

array = [1, 1, 2, 2, 2, 3]
print(array_123(array, 2))
