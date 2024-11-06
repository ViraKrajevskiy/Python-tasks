def array57(arr):
    even_elements = arr[1::2]
    odd_elements = arr[::2]
    b = even_elements + odd_elements
    print("Элементы массива b:", b)

array57([1, 2, 3, 4, 5, 6])
