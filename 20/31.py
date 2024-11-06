def IsPalindrome(N):
    N_str = str(N)
    return N_str == N_str[::-1]

print(IsPalindrome(12321))
print(IsPalindrome(12345))
