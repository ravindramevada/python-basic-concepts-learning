my_str1 = '{:.5}'.format('abcde')
print(my_str1)

my_str2 = '{:<15.5}'.format('abcde')
print(my_str2)

my_str3 = '{:-<15.5}'.format('abcde')
print(my_str3)

my_str4 = '{:>15.5}'.format('abcde')
print(my_str4)

my_str5 = '{:->15.5}'.format('abcde')
print(my_str5)

my_str6 = '{:^15.5}'.format('abcde')
print(my_str6)

my_str7 = '{:-^15.5}'.format('abcde')
print(my_str7)