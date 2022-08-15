'''
Valid identifiers: [a-z], [A-Z], [0-9] and _ (underscore).
The first character of an identifier cannot be a digit.
An identifier should not match a python keyword (reserved identifier).
'''
my_str1 = 'AbcdeAbcde'
x1 = my_str1.isidentifier()
print(x1)

my_str2 = 'Abcde_Abcde'
x2 = my_str2.isidentifier()
print(x2)

my_str3 = 'AbcdeAbcde20'
x3 = my_str3.isidentifier()
print(x3)