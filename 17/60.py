def array60(arr):
    b = []
    for i in range(len(arr)):
        b.append(sum(arr[i:]))
    print("Элементы массива b:", b)

array60([1, 2, 3, 4])
