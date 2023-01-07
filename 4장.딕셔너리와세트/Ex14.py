def restaurant():
    menu = {'sandwich':10, 'tea':7, 'coffee':5}
    total_cost = 0
    while True:
        a = input("Order :")
        # if len(a.strip()) == 0:
        if not a:
            break

        elif a in menu:
            total_cost += menu[a]
            print(f'{a} costs {menu[a]}, total is {total_cost}')
        elif a not in menu :
            print(f'Sorry, we are fresh out of {a} today')
    print(f'Your total is {total_cost}')

restaurant()
