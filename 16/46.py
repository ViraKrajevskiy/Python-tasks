def find_closest_sum_indices(arr, R):
    closest_sum = float('inf')
    index1, index2 = -1, -1

    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            current_sum = arr[i] + arr[j]
            if abs(current_sum - R) < abs(closest_sum - R):
                closest_sum = current_sum
                index1, index2 = i, j

    return index1, index2



arr = [1, 4, 3, 7, 10]
R = 8
print(find_closest_sum_indices(arr, R))