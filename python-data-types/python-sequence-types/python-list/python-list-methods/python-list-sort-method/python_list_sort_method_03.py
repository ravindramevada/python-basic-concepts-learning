def my_fun(elms):
    return len(elms)

my_lst = ['abc', 'ab', 'abcde', 'abcd', 'a']
my_lst.sort(key=my_fun)
print(my_lst)