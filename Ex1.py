import random

def guessing_game():
    number = random.randint(0, 100)
    print("맞춰야 하는 숫자 :", number)
    while True :
        guess_number = int(input("숫자를 맞춰보세요"))
        if number > guess_number:
            print("Too low")
        elif number < guess_number:
            print("Too high")
        else :
            print("Just Right")
            break

guessing_game()