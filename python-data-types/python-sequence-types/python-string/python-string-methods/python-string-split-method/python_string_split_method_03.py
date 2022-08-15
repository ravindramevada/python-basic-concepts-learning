import re

my_str1 = 'a,b;c:d'
x1 = re.split('[,;:]', my_str1)
print(x1)

my_str2 = 'a@bc$d'
x2 = re.split('[@$]', my_str2)
print(x2)

my_str3 = 'a@b#c$d'
x3 = re.split('[$#@]', my_str3)
print(x3)