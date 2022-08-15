my_str = 'the beginning is the end is the beginning'

x1 = my_str.rsplit(None, 1)
print(x1)

x2 = my_str.rsplit(None, 2)
print(x2)

x3 = my_str.rsplit(None, 3)
print(x3)

x4 = my_str.rsplit(None, 4)
print(x4)

x5 = my_str.rsplit(None, 5)
print(x5)

x6 = my_str.rsplit(None, 6)
print(x6)

x7 = my_str.rsplit(None, 7)
print(x7)

x8 = my_str.rsplit(None, -1) #  will make all possible rsplits (there is no limit on the number of rsplits)
print(x8)