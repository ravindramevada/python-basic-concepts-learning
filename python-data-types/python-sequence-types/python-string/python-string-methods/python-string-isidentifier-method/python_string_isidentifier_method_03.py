my_str = 'class'
x = my_str.isidentifier()
print(x)

import keyword
from keyword import iskeyword
print(iskeyword('class'))

def is_valid_identifier(my_str):
    return my_str.isidentifier() and not keyword.iskeyword(my_str)
print(is_valid_identifier('class'))

'''
A string is considered a valid identifier if
.isidentifier() returns True and iskeyword()
returns False.
'''