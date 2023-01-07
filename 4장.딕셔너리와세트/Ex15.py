def get_rainfall():
    result = {}
    while True :
        city_name = input("도시 이름을 입력하세요.")
        if not city_name :
            break

        city_rainfall = input("강수량을 입력하세요.")

        if city_name not in result.keys():
            result[city_name] = result.get(city_name, 0)
        result[city_name] += int(city_rainfall)

    for key, value in result.items():
        print(f'{key}, :  {value}')

get_rainfall()