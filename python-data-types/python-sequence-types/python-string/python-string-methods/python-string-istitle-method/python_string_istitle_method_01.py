my_str1 = 'Abcde Abcde'
x1 = my_str1.istitle()
print(x1)

my_str2 = 'Abcde Abcde - 123 @#$' # numbers and characters are ignored
x2 = my_str2.istitle()
print(x2)

my_str3 = 'Abcde abcde'
x3 = my_str3.istitle()
print(x3)

my_str4 = 'ABCDE ABCDE'
x4 = my_str4.istitle()
print(x4)

my_str5 = 'abcde abcde'
x5 = my_str5.istitle()
print(x5)