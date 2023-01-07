from datetime import datetime
from datetime import timedelta
def check_climate():
    climate_dict = {'2022-01-01':-1, '2022-01-02':-4, '2022-01-03': 0, '2022-01-04':3}
    today = input("날짜 입력").strip()
    if not today:
        print("날짜를 찾을 수 없습니다.")
    elif today in climate_dict.keys():

        yesterday = str(datetime.strptime(today, '%Y-%m-%d').date()-timedelta(1))
        tommorow = str(datetime.strptime(today, '%Y-%m-%d').date() + timedelta(1))
        if yesterday not in climate_dict.keys():
            print(f'오늘 기온 :{climate_dict[today]}, 내일 기온 :{climate_dict[tommorow]}')
        elif tommorow not in climate_dict.keys():
            print(f'어제 기온 :{climate_dict[yesterday]}, 오늘 기온 :{climate_dict[today]}')
        else:
            print(f'어제 기온:{climate_dict[yesterday]}, 오늘 기온:{climate_dict[today]}, 내일 기온 :{climate_dict[tommorow]}')

check_climate()