def array59(arr):
    b = []
    for i in range(len(arr)):
        b.append(sum(arr[:i+1]) / (i+1))
    print("Элементы массива b:", b)

array59([1, 2, 3, 4])
