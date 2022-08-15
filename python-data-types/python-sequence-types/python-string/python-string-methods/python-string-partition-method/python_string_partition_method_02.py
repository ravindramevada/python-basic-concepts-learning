'''
If the separator is not found, the method returns a tuple
containing two empty strings, followed by the string itself.
'''
my_str = 'the beginning is the end is the beginning'
x = my_str.partition('or')
print(x)