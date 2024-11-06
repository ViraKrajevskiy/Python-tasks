def array_129(array):
    max_series = []
    current_series = []
    previous_value = None

    for element in array:
        if element == previous_value:
            current_series.append(element)
        else:
            if len(current_series) >= len(max_series):
                max_series = current_series
            current_series = [element]
        previous_value = element

    if len(current_series) >= len(max_series):
        max_series = current_series

    return max_series

array = [1, 1, 2, 2, 3, 3, 3, 1, 1]
print(array_129(array))
