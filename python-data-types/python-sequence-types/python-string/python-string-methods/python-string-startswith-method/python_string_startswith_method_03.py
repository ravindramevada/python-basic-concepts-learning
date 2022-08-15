my_str = 'abcde'

pfx1 = ('b', 'bc')
x1 = my_str.startswith(pfx1)
print(x1)

pfx2 = ('b', 'bc', 'abc')
x2 = my_str.startswith(pfx2)
print(x2)