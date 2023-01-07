def cap_ubbi_dubbi(word):
    output = []
    for idx, element in enumerate(word):
        if idx == 0 and element.isupper() and element.lower() in 'aeiou':
            output.append(f'UB{element}')
        elif element in 'aeiou':
            output.append(f'ub{element}')
        else :
            output.append(element)
    return ''.join(output)


print(cap_ubbi_dubbi('Umbrella'))