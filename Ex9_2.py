def plus_minus(num_list):
    result = 0
    for idx in range(len(num_list)):
        if idx == 0:
            result += num_list[idx]
        elif idx % 2 == 0:
            result -= num_list[idx]
        else:
            result += num_list[idx]
    return result

print(plus_minus([10, 20, 30, 40, 50, 60]))

