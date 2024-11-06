import math

def IsSquare(K):
    if K > 0:
        root = int(math.sqrt(K))
        return root * root == K
    return False

print(IsSquare(9))
print(IsSquare(7))
