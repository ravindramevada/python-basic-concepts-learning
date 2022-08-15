my_str1 = 'abcde abcde'
x1 = my_str1.split()
print(x1)

my_str2 = ' abcde abcde '
x2 = my_str2.split()
print(x2)

my_str3 = 'abcde, abcde'
x3 = my_str3.split(', ')
print(x3)

my_str4 = 'abcde\nabcde'
x4 = my_str4.split('\n')
print(x4)

my_str5 = 'the beginning is the end is the beginning'
x5 = my_str5.split(' is ')
print(x5)