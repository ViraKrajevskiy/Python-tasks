import random

a = random.randint(4,20)
b = -10
c = random.randint(4,20)

if a > 0 and c > 0 and b < 0:
   print(True)
elif a > 0 and b > 0 and c < 0 :
   print(True)
elif c > 0 and b > 0 and a < 0 :
    print(True)
else:
    print(False)
