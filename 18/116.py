
def array_116(array):
    series_lengths = []
    current_series = []
    previous_value = None

    for element in array:
        if element == previous_value:
            current_series.append(element)
        else:
            if current_series:
                series_lengths.append(len(current_series))
            current_series = [element]
        previous_value = element

    if current_series:
        series_lengths.append(len(current_series))

    return series_lengths

array = [1, 1, 2, 2, 2, 3, 1, 1]
print(array_116(array))
