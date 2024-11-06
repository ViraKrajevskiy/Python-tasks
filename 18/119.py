def array_119(array):
    result = []
    previous_value = None

    for element in array:
        if element != previous_value:
            result.append(element)  # Добавляем сам элемент перед серией
        result.append(element)
        previous_value = element

    return result

array = [1, 1, 2, 2, 3]
print(array_119(array))
