my_str = 'abcde'

suff1 = ('d', 'cd')
x1 = my_str.endswith(suff1)
print(x1)

suff2 = ('d', 'cd', 'cde')
x2 = my_str.endswith(suff2)
print(x2)