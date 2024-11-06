def find_unordered_element(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return arr[i + 1]
    return "Все элементы упорядочены"

arr = [1, 2, 3, 7, 5, 9]
print(find_unordered_element(arr))
