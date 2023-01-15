# 입력파일의 이름을 나타내는 1개의 필수 매개변수와 이를 복사해서 출력할 이름을 나타내는 여러 개의 옵션 매개변수를 갖는 copyfile 함수 만들기

def copyfile(filename, *copyfilename):
    if not copyfilename:
        with open(filename, 'r') as input:
            for line in input:
                print(line)
    else:
        for name in copyfilename :
            with open(name, 'w') as output:
                with open(filename, 'r') as input:
                    for line in input:
                        output.write(line)



print(copyfile('.\myfile.txt', 'copy1.txt', 'copy2.txt'))