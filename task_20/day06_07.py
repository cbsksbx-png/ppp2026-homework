import matplotlib.pyplot as plt
import numpy as np
import requests
import os
import pandas as pd
import koreanize_matplotlib

def download_weather(name, stid, sy, ey):

    URL = f"https://api.taegon.kr/stations/{stid}/?sy={sy}&ey={ey}&format=csv"

    filename = f"weather_{name}_{sy}_{ey}.csv"

    if not os.path.exists(filename):
        resp = requests.get(URL)
        with open(filename, "w", encoding="UTF-8-sig") as fout:
            fout.write(resp.text)
    else:
        print(f"이미 {filename}이 있습니다.")


def main():
    filename = "weather_jeonju_1980_2024.csv"

    download_weather("jeonju", 146, 1980, 2024)

    df = pd.read_csv(filename, skipinitialspace = True)

    month = int(input('월 입력'))
    date = int(input('일 입력'))
    # date = df['month'],df['day']
    year = np.array(df['year'].unique())

    # print(date)
    tavg = []
    day = df[(df['month'] == month) & (df['day'] == date)]
    print(day['tavg'])
    tavg.append(np.array(day['tavg']))

    plt.plot(day['year'], day['tavg'], color="g", label="전주_tavg")
    plt.xlabel("연도")
    plt.ylabel("온도(℃)")

    plt.savefig(f"./{month}월 {date}일 온도 꺽은선 그래프.png")

    max(day['tavg'])

    sorted_day = day.sort_values(by='tavg', ascending=False)
    # 정렬 day에서 온도 기준으로 내림차순으로 정렬 sort_values 데이터를 특정 기준으로 정렬시 사용하는 함수

    print("최고 온도 연도:", sorted_day.iloc[0]['year'])
    print("최저 온도 연도:", sorted_day.iloc[-1]['year'])
    # iloc란 각 이름을 숫자로 표시한것 즉 0 -> 1980, 16070 -> 2024 로
    # 즉 sorted_day.iloc[0]['year'] 란 day 를 정렬한 부분에서 맨압에를 년도로 환산한 년도가 나오고 sorted_day.iloc[-1]['year'] 맨뒤를 환산한 연도가 나옴


    birth_year = int(input("태어난 연도 입력: "))
    rank_df = sorted_day.reset_index(drop=True)
    # reset_index는 정렬된 결과를 0부터 다시 번호 매겨서 순위처럼 쓰기에
    # 여기에 +1을 해야 정확한 들수가 나옴 그러기에 및에서 내 생일연도가 'year'랑 값이 같을때의 값 에 +1을 한이유


    my_rank = rank_df[rank_df['year'] == birth_year].index[0] + 1
    print("내 생일 온도 순위:", my_rank)


    # print(rainfall)

if __name__ == "__main__":
    main()