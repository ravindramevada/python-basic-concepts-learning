my_str1 = '123'
x1 = my_str1.isdecimal()
print(x1)

my_str2 = '\u0030' # unicode decimal character 0 (U+0030)
x2 = my_str2.isdecimal()
print(x2)