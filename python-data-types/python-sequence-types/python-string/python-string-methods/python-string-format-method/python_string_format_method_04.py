my_str1 = '{:<15}'.format('abcde')
print(my_str1)

my_str2 = '{:-<15}'.format('abcde')
print(my_str2)

my_str3 = '{:>15}'.format('abcde')
print(my_str3)

my_str4 = '{:->15}'.format('abcde')
print(my_str4)

my_str5 = '{:=5d}'.format(+20) # add padding between sign & digits (valid for numbers only)
print(my_str5)

my_str6 = '{:0=5d}'.format(+20) # add padding between sign & digits (valid for numbers only)
print(my_str6)

my_str7 = '{:=5d}'.format(-20)
print(my_str7)

my_str8 = '{:0=5d}'.format(-20)
print(my_str8)

my_str9 = '{:^15}'.format('abcde')
print(my_str9)

my_str10 = '{:-^15}'.format('abcde')
print(my_str10)