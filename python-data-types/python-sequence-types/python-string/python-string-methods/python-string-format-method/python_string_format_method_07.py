my_str1 = '{:e}'.format(3141592653)
print(my_str1)

my_str2 = '{:.2e}'.format(3141592653)
print(my_str2)

my_str3 = '{:.2E}'.format(3141592653)
print(my_str3)

print('')

my_str4 = '{:f}'.format(3.141592653)
print(my_str4)

my_str5 = '{:.2f}'.format(3.141592653)
print(my_str5)

print('')

# f vs F
my_str6 = '{:f}'.format(float('NAN'))
print(my_str6)

my_str7 = '{:f}'.format(float('INF'))
print(my_str7)

my_str8 = '{:F}'.format(float('nan'))
print(my_str8)

my_str9 = '{:F}'.format(float('inf'))
print(my_str9)

print('')

my_str10 = '{:%}'.format(12/20)
print(my_str10)

my_str11 = '{:.2%}'.format(12/20)
print(my_str11)