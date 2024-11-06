def Fib(N):
    a, b = 0, 1
    for _ in range(1, N):
        a, b = b, a + b
    return b

print(Fib(7))
