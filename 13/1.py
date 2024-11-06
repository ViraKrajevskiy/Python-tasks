from random import randrange

k = randrange(0,10000000)
s = 0
count = 0

print(k)
while k > 0:
    r = k% 10
    if r % 2 ==0:
        s+=r
        count +=1

    k//=10
    print(k)

