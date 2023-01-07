### 내가 푼 답
# def hex_output(hex_number):
#     result = 0
#     for idx in range(len(str(hex_number))):
#         result += int(str(hex_number)[::-1][idx])*(16**idx)
#
#     return result
#
# print(hex_output(32))


### 책에 써 있는 답
def hex_output():
    decnum = 0
    hexnum = input("Enter ahex number to convert:")
    for power, digit in enumerate(reversed(hexnum)):
        decnum += int(digit, 16) * (16 ** power)
    print(decnum)

hex_output()
