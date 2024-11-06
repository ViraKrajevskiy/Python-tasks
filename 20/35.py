def Fact2(N):
    result = 1
    for i in range(N, 0, -2):
        result *= i
    return result

print(Fact2(5))
