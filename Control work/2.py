b = int(input())
a = int(input())

c = []
if a<b:
    for i in range(a,b+1):
           c.append(i)

print(sum(c))