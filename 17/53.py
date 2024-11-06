def sum_of_two_arrays(A, B):
    return [A[i] + B[i] for i in range(len(A))]

A = [1, 2, 3]
B = [4, 5, 6]
print(sum_of_two_arrays(A, B))
