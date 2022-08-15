def my_fun(elm):
    return elm[1]

my_lst = [(3, 4), (1, 2), (7, 8), (5, 6)]
my_lst.sort(key=my_fun)
print(my_lst)