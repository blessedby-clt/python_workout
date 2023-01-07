## 매개변수로 받은 문자열을 유니코드 순서로 정렬
def strsort(word):
    return ''.join(sorted(word))
print(strsort("hello python"))