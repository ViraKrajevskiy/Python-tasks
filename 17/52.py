def swap_elements_if_less(A, B):
    for i in range(len(A)):
        if A[i] < 5:
            A[i], B[i] = B[i], A[i]
    return A, B

A = [3, 6, 2, 7]
B = [9, 5, 8, 4]
print(swap_elements_if_less(A, B))
