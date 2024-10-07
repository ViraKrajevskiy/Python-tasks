a = int(input())
b = int(input())
d = int(input())

c = a < 0 and b < 0 and d < 0 or a > 0 and b > 0 and d > 0
print(c)