my_str1 = '{a}{b}'.format(a='abcde', b='fghij')
print(my_str1)

my_tpl = ('abcde', 'fghij')
my_str2 = '{0[0]}{0[1]}'.format(my_tpl)
print(my_str2)

my_dict = {'a':'abcde', 'b':'fghij'}
my_str3 = '{a}{b}'.format(**my_dict)
print(my_str3)