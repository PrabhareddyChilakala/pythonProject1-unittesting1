def search_num_list(target):
    list = [1, 4, 34, 67, 90, 45]
    for i in list:
        if i==target:
            return list.index(target)
        else:
            continue

target=int(input("enter number to search:"))
print(search_num_list(target))