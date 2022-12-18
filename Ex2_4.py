def mysum(list_element):
    result = 0
    for idx in list_element:
        if str(idx).isnumeric():
            result += idx
    return result

print(mysum([1,2,4,"apple", "angle", 3, "banana"]))