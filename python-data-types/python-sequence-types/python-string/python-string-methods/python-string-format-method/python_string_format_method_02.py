my_str1 = '{0}{1}'.format('abcde', 'fghij')
print(my_str1)

my_str2 = '{1}{0}'.format('fghij', 'abcde')
print(my_str2)

my_str3 = '{0}{1}{0}'.format('abcde', 'fghij')
print(my_str3)

my_str4 = '{}{}{}{}{}'.format(*'abcdefghij') # unpacking argument sequence
print(my_str4)

my_str5 = '{1}{3}{5}{7}{9}'.format(*'abcdefghij')
print(my_str5)