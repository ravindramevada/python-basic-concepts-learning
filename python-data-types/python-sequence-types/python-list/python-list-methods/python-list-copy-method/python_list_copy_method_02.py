my_lst1 = [1, 2, 3, 4, 5]
x1 = my_lst1
print(x1)
my_lst1[2] = 6
print(my_lst1)
print(x1)
print(x1 is my_lst1)

print('')

my_lst2 = [1, 2, 3, 4, 5]
x2 = my_lst2.copy()
print(x2)
my_lst2[2] = 6
print(my_lst2)
print(x2)
print(x2 is my_lst2)