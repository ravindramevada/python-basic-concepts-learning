a1 = 10
b1 = 20
a2 = -10
b2 = -20
print(~a1)
print(~b1)
print(~a2)
print(~b2)

'''
a1 = 10: 0000 1010
~a1 = ~0000 1010
    = -(0000 1010 + 1)
    = -(0000 1011)
    = - 11

b1 = 20: 0001 0100
~b1 = ~0001 0100
    = -(0001 0100 + 1)
    = -(0001 0101)
    = -21

a2 = -10: 1111 0110
~a2 = ~1111 0110
    = -(1111 0110 + 1)
    = -(1111 0111)
    = -(-9)
    = 9

b2 = -20: 1110 1100
~b2 = ~1110 1100
    = -(1110 1100 + 1)
    = -(1110 1101)
    = -(-19)
    = 19
'''