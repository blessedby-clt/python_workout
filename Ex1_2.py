import random

word_list = ['apple', 'banana', 'cat', 'dice', 'egg', 'friend', 'girl', 'hello', 'ice', 'juice',
             'kite', 'opportunity', 'lemon', 'money', 'nice']
word_list.sort()
def guess_word():
    target_idx = random.randint(0, len(word_list) - 1)
    while True:
        print(word_list)
        input_word = input("단어를 맞혀주세요.")
        try:
            if word_list.index(input_word) > target_idx:
                print("사전 순서에서 더 앞에 있는 단어입니다.")
            elif word_list.index(input_word) > target_idx:
                print("사전 순서에서 더 뒤에 있는 단어입니다.")
            else:
                print("단어를 맞추셨습니다.")
                break
        except:
            print("없는 단어입니다.")


guess_word()

