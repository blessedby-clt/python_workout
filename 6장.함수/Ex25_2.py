def multiplyAll(*numbers):
    result = 1
    for number in numbers:
        result *= number
    return result

print(multiplyAll(2,3,2,11))