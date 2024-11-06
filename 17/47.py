def unique_elements(arr):
    seen = set()
    result = []
    for num in arr:
        if num not in seen:
            result.append(num)
            seen.add(num)
    return result

arr = [7, 4, 2, 3, 1, 4, 5, 2, 4, 7]
print(unique_elements(arr))
