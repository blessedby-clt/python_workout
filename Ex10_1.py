def mysum_bigger_than(target_number, *args):
    result = 0
    for i in args:
        if i > target_number:
            result += i
    return result

print(mysum_bigger_than(10,5,20,30,6))