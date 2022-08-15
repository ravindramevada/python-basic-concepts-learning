my_str = 'abcde'
print(len(my_str))

print('')

print(my_str)

x1 = my_str.ljust(5, '-') # the original string is returned as it is, if width is less than or equal to string length
print(x1)

x2 = my_str.ljust(6, '-')
print(x2)

x3 = my_str.ljust(7, '-')
print(x3)