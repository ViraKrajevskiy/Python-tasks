def IsPowerN(K, N):
    while K > 1 and K % N == 0:
        K //= N
    return K == 1

print(IsPowerN(8, 2))
print(IsPowerN(12, 3))
