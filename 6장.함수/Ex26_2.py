def print_hello(name):
    return f'Hello {name}!'

def apply_to_each(func, iter):
    # result = iter
    result = list()

    for value in iter:
        result.append(func(value))
    return result

print(apply_to_each(print_hello, ('Jo', 'MG', 'Jack')))

