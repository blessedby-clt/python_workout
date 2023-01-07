def mysum_dict(*args):
    my_dict = {}
    for element in args:
        for key, value in element.items():
            if key not in my_dict:
                my_dict[key] = my_dict.get(key, [])
                my_dict[key].append(value)
            else:
                my_dict[key].append(value)
    return my_dict
print(mysum_dict({'a':1, 'b':2}, {'c':[1,3], 'd':[2,4]}, {'c':2}, {'d':[3,5]}))