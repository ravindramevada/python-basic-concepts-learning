my_str1 = '{:+f}; {:+f}'.format(3.14, -3.14) # shows sign always
print(my_str1)

my_str2 = '{: f}; {: f}'.format(3.14, -3.14) # shows a space for positive numbers
print(my_str2)

my_str3 = '{:-f}; {:-f}'.format(3.14, -3.14) # shows a minus (-) for negative numbers
print(my_str3)