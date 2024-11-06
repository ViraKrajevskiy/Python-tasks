a = [1, 23, 4, 6, 7, 12, 23, 34, 57, 4, 5, 8, 99, 10, 14]
filtered_list = list(filter(lambda x: x % 2 == 0 , a ))
print(filtered_list)
s = []

new_lst = [s + 1 for s in filtered_list ]
print(new_lst)