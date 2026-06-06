import matplotlib.pyplot as plt
import numpy as np
import koreanize_matplotlib
import pandas as pd


def main():
    # dices = np.random.randint(1, 7, size=100) # random 모듈과 다름
    # print(dices)

    df_jj = pd.read_csv("weather_jeonju_1980_2024.csv",skipinitialspace=True)

    year_tavg_jj = []
    for i in range(1980, 2025):
        year_tavg_jj.append(round(df_jj[df_jj["year"] == i]["rainfall"].sum(), 1))
    tavg_jj = np.array(year_tavg_jj)

    # print(tavg_jj)

    year = np.array(df_jj['year'].unique())

    # print(yearly_tavg_jj)

    plt.bar(year, tavg_jj, color="b")
    plt.xlabel("연도")
    plt.ylabel("강수량")

    # 1이 몇개 2가 몇개 3이 몇개인 히스토그램
    # plt.show()
    plt.savefig("./1980년도 부터 2024년 까지 전주시 강수량.png")

if __name__ == '__main__':
    main()
