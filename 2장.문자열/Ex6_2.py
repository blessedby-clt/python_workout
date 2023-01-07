def make_new_list(word_list):
    new_list = []
    for word in word_list:
        new_list.append(word.split())
        print(new_list)
    return [" ".join(element) for element in zip(*new_list)]



print(make_new_list(['abc def ghi', 'jkl mno pqr', 'stu vwx yz']))
