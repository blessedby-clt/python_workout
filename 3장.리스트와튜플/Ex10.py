def mysum(*args):
    if not args:
        return args
    else:
        output = args[0]
        for i in args[1:]:
            output += i
        return output

print(mysum([1,2,3], [4,5,6]))
print(mysum('abc', 'def'))
print(mysum(('a','b'),('c','d')))