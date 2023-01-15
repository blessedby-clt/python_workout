def myxml(tag, contents = '', **attr):

    attr_string = ''
    for key, value in attr.items():
        attr_string += f'{key}="{value}"'
    result = f'<{tag} {attr_string}>{contents}</{tag}>'
    return result

print(myxml('foo', 'bar', a=1, b=2, c=3))