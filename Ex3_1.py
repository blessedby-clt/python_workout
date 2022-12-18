def split_decimal(number, before, after):
    str_number = str(number)
    print(float(str_number.split(".")[0][-before:]+"."+str_number.split(".")[1][:after]))

split_decimal(1234.56789, 2, 3)