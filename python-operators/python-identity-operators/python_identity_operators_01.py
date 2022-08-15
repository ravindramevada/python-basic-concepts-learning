x = ['a', 'b']
y = ['a', 'b']
z = x
print(x is z) # x is the same object as z
print(x is y) # x is not the same object as y, even if they have the same content.
'''
They are equal but not identical. It is because the interpreter
locates them separately in memory although they are equal.
'''
print(x == y) # difference between 'is' and '=='