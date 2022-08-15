my_str = 'Abcde\nAbcde' # carriage return \r, line feed \n and tab \t are non-printable characters
x = my_str.isprintable()
print(x)