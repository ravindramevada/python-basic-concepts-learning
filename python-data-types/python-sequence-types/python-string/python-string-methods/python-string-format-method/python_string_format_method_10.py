import datetime
date = datetime.datetime(2000, 12, 20, 6, 20, 00)
my_str = '{:%Y-%m-%d %H:%M:%S}'.format(date) # datetime formatting
print(my_str)