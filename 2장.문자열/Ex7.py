## 내가 푼 내용
def ubbi_dubbi(word):
    new_word = ''
    for element in word:
        if element in 'aeiou':
            new_word += 'ub'+element
        else :
            new_word += element
    return new_word

### 책에 적힌 내용
def ubbi_dubbi(word):
    output = []
    for letter in word:
        if letter in 'aeiou':
            output.append(f'ub{letter}')
        else :
            output.append(letter)
    return ''.join(output)
## 메모리를 효율적으로 사용하기 위해서 문자열 연결을 사용하지 않고 리스트 활용.

print(ubbi_dubbi('python'))