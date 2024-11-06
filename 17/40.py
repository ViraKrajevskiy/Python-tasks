def closest_element(arr, R):
    return min(arr, key=lambda x: ((x - R) if (x - R) >= 0 else (R - x), x))

arr = [3, 8, 9, 15, 17]
R = 10
print(closest_element(arr, R))
