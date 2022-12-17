import random

def guessing_game():
    number = random.randint(0, 100)
    chance_count = 3
    print("맞춰야 하는 숫자 :", number)
    while chance_count > 0 :
        guess_number = int(input("숫자를 맞춰보세요"))
        if number > guess_number:
            print("Too low")
            chance_count -= 1
            print("남은 횟수", chance_count, "번")
        elif number < guess_number:
            print("Too high")
            chance_count -= 1
            print("남은 횟수", chance_count, "번")
        else :
            print("Just Right")
            break
    if chance_count == 0 :
        print("3번의 기회 안에 맞추지 못해 프로그램을 종료합니다.")
    else :
        print("축하합니다. 정답을 맞히셨습니다.")

guessing_game()