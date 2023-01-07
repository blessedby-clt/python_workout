def mysum(*args) :
    print(type(args))
    # print(*args)
    result = 0
    for i in args :
        result += i
    return result

print(mysum(*[1,2,3,4,5,6]))