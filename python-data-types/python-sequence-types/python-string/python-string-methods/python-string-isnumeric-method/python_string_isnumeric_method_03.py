# isnumeric() vs isdecimal() vs isdigit()

# decimal number 0 (U+0030)
print('\u0030'.isnumeric())
print('\u0030'.isdecimal())
print('\u0030'.isdigit())

print('')

# subscript two ₂ (U+2082)
print('\u2082'.isnumeric())
print('\u2082'.isdecimal())
print('\u2082'.isdigit())

print('')

# superscript two ² (U+00B2)
print('\u00b2'.isnumeric())
print('\u00b2'.isdecimal())
print('\u00b2'.isdigit())

print('')

# vulgar fraction one third ⅓ (U+2153)
print('\u2153'.isnumeric())
print('\u2153'.isdecimal())
print('\u2153'.isdigit())

print('')

# roman numerals Ⅰ (U+2160)
print('\u2160'.isnumeric())
print('\u2160'.isdecimal())
print('\u2160'.isdigit())

print('')

# currency numerators ৴ (bengali currency numerators one - U+09F4)
print('\u09f4'.isnumeric())
print('\u09f4'.isdecimal())
print('\u09f4'.isdigit())

'''
isdecimal(): Decimal Numbers
isdigit(): Decimals, Subscripts, Superscripts
isnumeric(): Digits, Vulgar Fractions, Subscripts, Superscripts, Roman Numerals, Currency Numerators
'''