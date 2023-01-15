## 함수가 데이터로 취급되는 부분이 계속 이해가 잘되지 않는다.

import operator

def calc(to_solve):
    operations = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv,
        '**': operator.pow,
        '%' : operator.mod
    }

    op, first_s, second_s, *args = to_solve.split()
    result = operations[op](int(first_s), int(second_s))
    for i in args:
        result = operations[op](result, int(i))

    return result


print(calc('+ 1 2 3 4 5 6 7 8 9 10'))