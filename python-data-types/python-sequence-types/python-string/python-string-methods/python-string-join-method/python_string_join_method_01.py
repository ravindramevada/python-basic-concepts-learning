my_lst1 = ['a', 'b', 'c']
x1 = ', '.join(my_lst1)
print(x1)

my_lst2 = ['the beginning', 'the end', 'the beginning']
x2 = ' is s'.join(my_lst2)
print(x2)

my_lst3 = ['a']
x3 = ','.join(my_lst3)
print(x3)

my_lst4 = [1, 2, 3, 4, 5]
x4 = ', '.join(str(val) for val in my_lst4)
print(x4)

my_lst5 = ['a', 'b', 'c']
x5 = '\t'.join(my_lst5)
print(x5)