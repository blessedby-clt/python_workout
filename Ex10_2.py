def sum_numeric(*args):
    result = 0
    for element in args:
        if str(element).isnumeric():
            result += int(element)
    return result

print(sum_numeric(10, 20, 'a', '30', 'abc'))