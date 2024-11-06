def array58(arr):
    b = []
    for i in range(len(arr)):
        b.append(sum(arr[:i+1]))
    print("Элементы массива b:", b)

array58([1, 2, 3, 4])
