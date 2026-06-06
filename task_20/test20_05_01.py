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

    filename_jj = "weather_jeonju_1980_2024.csv"
    filename_sw = "weather_suwon_1980_2024.csv"



    download_weather("jeonju", 146, 1980, 2024)
    download_weather("suwon", 119, 1980, 2024)

    df_jj = pd.read_csv(filename_jj, skipinitialspace = True)
    df_sw = pd.read_csv(filename_sw, skipinitialspace = True)

    # print(df_jj)
    year_tavg_jj = []
    for i in range(1980,2025):
        year_tavg_jj.append(round(df_jj[df_jj["year"] == i]["tavg"].mean(), 1))

    year_tavg_sw = []
    for i in range(1980, 2025):
        year_tavg_sw.append(round(df_sw[df_sw["year"] == i]["tavg"].mean(), 1))

    print(year_tavg_jj)

    tavg_jj = np.array(year_tavg_jj)
    tavg_sw = np.array(year_tavg_sw)

    # print(tavg_jj)

    year = np.array(df_jj['year'].unique())

    year = np.array(df_sw['year'].unique())
    # print(year)

    # yearly_tavg_jj = year, tavg_jj
    # print(yearly_tavg_jj)

    # 현재까지 앞에는 연도 리스트, 뒤에는 tavg 값의 합이 있음 이거만 해결하면 되는디 반복문을 써서 하면 될거같음!

    # tavg_sw = df_sw['tavg']

    # yearly_tavg_jj_ye = yearly_tavg_jj,tavg_jj



    plt.plot(year, tavg_jj, color="g", label="전주_tavg")
    # plt.plot(yearly_tavg_sw, color="b", label="수원_tavg")
    plt.ylabel("온도(℃)")
    plt.legend()
    # plt.show()
    plt.savefig("./전주,수원 tavg 꺽은선 그래프.png")

if __name__ == "__main__":
    main()
