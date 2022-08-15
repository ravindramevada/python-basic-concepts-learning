def my_fun(elm):
    return elm['y']

my_lst = [
    {'x': 'a', 'y': 2},
    {'x': 'b', 'y': 4},
    {'x': 'c', 'y': 1},
    {'x': 'd', 'y': 3},
]
my_lst.sort(key=my_fun)
print(my_lst)