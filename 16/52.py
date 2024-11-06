def create_b_array(a):
    b = []
    for elem in a:
        if elem < 5:
            b.append(2 * elem)
        else:
            b.append(elem / 2)
    return b

a = [3, 7, 4, 8, 1]
b = create_b_array(a)
print(b)