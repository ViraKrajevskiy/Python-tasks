def IsPrime(N):
    if N <= 1:
        return False
    for i in range(2, int(N ** 0.5) + 1):
        if N % i == 0:
            return False
    return True

print(IsPrime(7))
print(IsPrime(10))
