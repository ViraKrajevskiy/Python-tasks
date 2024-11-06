def IsPower5(K):
    while K > 1 and K % 5 == 0:
        K //= 5
    return K == 1

print(IsPower5(25))
print(IsPower5(30))
