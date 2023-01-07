def make_dict(*args):
    result = {}
    for idx in range(len(args)):
        if idx % 2 == 0:
            result.get(args[idx])
        else:
            result[args[idx - 1]] = args[idx]

    return result

print(make_dict('a', 1, 'b', 2))


