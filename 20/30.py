def DigitN(K, N):
    K_str = str(abs(K))
    return int(K_str[N - 1]) if 1 <= N <= len(K_str) else -1

print(DigitN(12345, 2))
print(DigitN(12345, 6))
