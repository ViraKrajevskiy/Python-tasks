a = int(input())
b = int(input())
c = a%2 == 1 and b% 2 == 0 or a%2 == 0 and b%2 == 0
print(c)