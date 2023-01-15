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

    op, first_s, second_s = to_solve.split()
    first_s = int(first_s)
    second_s = int(second_s)
    return operations[op](first_s, second_s)

print(calc('% 5 3'))