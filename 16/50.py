def count_elements_greater_than_right_neighbour(arr):
    count = 0

    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            count += 1

    return count

arr = [2, 5, 1, 7, 3, 9]
print(count_elements_greater_than_right_neighbour(arr))