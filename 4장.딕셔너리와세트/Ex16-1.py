def dictadd(first, *args):
    result = first
    for dict_arg in args:
        result.update(dict_arg)

    return result

d1 = {'a':1, 'b':2, 'c':3}
d2 = {'a':1, 'b':2, 'c':4}
d3 = {'a':1, 'b':2, 'd':3}
d5 = {'a':1, 'b':2, 'd':4}
print(dictadd(d1, d2, d3))