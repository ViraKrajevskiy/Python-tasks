def create_c_array(a, b):
    c = []
    for i in range(len(a)):
        c.append(max(a[i], b[i]))
    return c

a = [1, 4, 3]
b = [2, 3, 5]
c = create_c_array(a, b)
print(c)