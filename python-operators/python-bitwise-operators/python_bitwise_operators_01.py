a1 = 10
b1 = 20
a2 = -10
b2 = -20
print(a1 & b1)
print(a2 & b2)

'''
&:
a b  y
0 0  0
0 1  0
1 0  0
1 1  1

a1 = 10: 0000 1010
b1 = 20: 0001 0100
a1 & b1: 0000 0000 = 0

a2 = -10: 1111 0110
b2 = -20: 1110 1100
a2 & b2:  1110 0100 = -28
'''