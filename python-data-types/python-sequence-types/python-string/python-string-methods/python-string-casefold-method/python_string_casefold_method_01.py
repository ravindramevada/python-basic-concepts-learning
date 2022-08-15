my_str = 'Claß'
x = my_str.casefold()
print(my_str)
print(x)

print('')

my_str1 = 'Claß'
my_str2 = 'class'
if my_str1.casefold() == my_str2:
    print('Equal')
else:
    print('Not equal')

my_str1 = 'Claß'
my_str2 = 'Class'
if my_str1.casefold() == my_str2.casefold():
    print('Equal')
else:
    print('Not equal')

'''
casefold() vs lower():
casefold() and lower() converts the string to lowercase,
but casefold() converts even the caseless letters such as
the ß in German to ss.
'''