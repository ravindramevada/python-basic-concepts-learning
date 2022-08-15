my_str1 = '{:,d}'.format(1234567890) # thousand separator
print(my_str1)

my_str2 = '{:_d}'.format(1234567890) # underscore as a thousand separator
print(my_str2)

my_str3 = '{:_b}'.format(0b1010101010) # underscore as a nibble separator
print(my_str3)