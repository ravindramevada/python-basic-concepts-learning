my_str1 = 'the beginning is the end'
x1 = my_str1.rpartition('is')
print(x1)

my_str2 = 'the end is the beginning'
x2 = my_str2.rpartition('is')
print(x2)

my_str3 = 'the beginning is the end is the beginning'
x3 = my_str3.rpartition('is')
print(x3)