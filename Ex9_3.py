def myzip(*args):
    return [i for i in zip(*args)]

print(myzip([10, 20, 30], 'abc'))

# 'abc'