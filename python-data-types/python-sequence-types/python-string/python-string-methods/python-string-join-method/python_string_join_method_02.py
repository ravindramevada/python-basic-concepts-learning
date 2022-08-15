my_dict1 = {'x':'a', 'y':'b'}
x1 = ', '.join(my_dict1)
print(x1)

my_dict2 = {'x':'a', 'y':'b'}
x2 = ', '.join(my_dict2.values())
print(x2)

my_dict3 = {'a':1, 'b':2}
x3 = ', '.join(str(val) for val in my_dict3.values())
print(str(x3))

my_dict4 = {'x':'a', 'y':'b'}
x4 = ', '.join('='.join((key, val)) for (key, val) in my_dict4.items())
print(x4)
