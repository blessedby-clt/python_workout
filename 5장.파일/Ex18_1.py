def get_digit_case(filename):
    with open(filename, 'r') as f:
        for line in f:
            line = line.replace('\n', '')
            result = 0
            for word in line:
                if word.isdigit():
                    result += 1
            print(f'{line} : {result}')


get_digit_case('etc/passwd')