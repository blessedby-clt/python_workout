def mysum(list_num, unique_num=0):
    result = 0
    for number in list_num :
        result += number
    return result + unique_num

print(mysum([1,2,3,4],5))