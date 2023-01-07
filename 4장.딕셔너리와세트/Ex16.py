d1 = {'a':1, 'b':2, 'c':3}
d2 = {'a':1, 'b':2, 'c':4}
d3 = {'a':1, 'b':2, 'd':3}
d5 = {'a':1, 'b':2, 'd':3}

## 내가 푼 내용
def dictdiff(dict1, dict2):
    key_list = []
    for i in dict1.keys():
        key_list.append(i)
    for j in dict2.keys():
        key_list.append(j)
    key_set = list(set(key_list))
    result = {}
    for key in key_set:

        if key in dict1.keys():
            if key in dict2.keys():
                if dict1[key] != dict2[key]:
                    result[key] = result.get(key, [dict1[key], dict2[key]])
            else:
                result[key] = result.get(key, [dict1[key], None])
        else:
            if key in dict2.keys():
                result[key] = result.get(key, [None, dict2[key]])

    return result

## 책 코드
def dictdiff(first, second):
    output = {}
    all_keys = first.keys() | second.keys()
    
    for key in all_keys:
        if first.get(key) != second.get(key):
            output[key] = [first.get(key), second.get(key)]
    return output


print(dictdiff(d1, d2))
print(dictdiff(d3, d2))
print(dictdiff(d1, d5))