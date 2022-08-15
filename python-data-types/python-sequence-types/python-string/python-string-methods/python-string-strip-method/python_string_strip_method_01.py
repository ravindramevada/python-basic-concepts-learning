my_str1 = '     abcde     '
x1 = my_str1.strip()
print(x1)

print('')

my_str2 = '     abcde  abcde     '
x2 = my_str2.strip()
print(x2)

print('')

my_str3 = '  \n  abcde  abcde     ' # carriage return (/r), tab(\t) and new line (\n)
x3 = my_str3.strip()
print(x3)
