from collections import Counter

def most_frequent_element(arr):
    return Counter(arr).most_common(1)[0][0]

arr = [7, 4, 7, 4, 2, 7]
print(most_frequent_element(arr))
