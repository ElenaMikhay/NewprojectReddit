list1 = [1, 4, 5, 6, 8]
list2 = [1, 2, 3, 4, 9]
list3 = ([value for value in list2 if not value in list1]+[value for value in list1 if not value in list2])


print(list3)
