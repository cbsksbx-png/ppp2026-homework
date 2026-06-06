import requests
import os.path
import pandas as pd

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
    filename_sw = "weather_suwon_1980_2024.csv"



    download_weather("jeonju", 146, 1980, 2024)
    download_weather("suwon", 119, 1980, 2024)

    df_jj = pd.read_csv(filename, skipinitialspace = True)
    df_sw = pd.read_csv(filename_sw, skipinitialspace = True)

    # print(df_jj.head())
    # 1) 전주시의 2012년 연 강수량은?
    print(f"전주시의 2012년 연강수량은 {df_jj[df_jj["year"] == 2012]["rainfall"].sum().round(1)}입니다.")
    # 강수량은 1359
    print(f"전주시의 2012년 연강수량은 {df_jj[df_jj["year"] == 2012]["rainfall"].sum().round(1) / 365:.1f}입니다.")
    # 연강수량의 평균 3.7

    # 2) 전주시의 2024년 최대기온은?
    print(f"2024년 전주시 최대기온은 {df_jj[df_jj["year"] == 2024]["tmax"].max()}입니다.")

    # 3) 전주시의 2020년 최대 일교차는?
    df_jj["tdiff"] = df_jj["tmax"] - df_jj["tmin"]
    print(f"전주시의 2020년 최대 일교차는 {df_jj[df_jj["year"] == 2024]["tdiff"].max()}입니다.")

    # 4) 수원시(119)와 전주시(146)의 2019년 총강수량 차이는(절대값)?
    prec_jj = df_jj[df_jj["year"] == 2019]["rainfall"].sum()
    prec_sw = df_sw[df_sw["year"] == 2019]["rainfall"].sum()
    print(f"전주시와 수원시의 2019년 총강수량의 차이는 {abs(prec_jj - prec_sw)}입니다.")

    # 5) 1980년 부터 2024년 까지 전주시, 수원시 평균기온을 선그래프로 그리시오
    # 6) 1980년부터 2024년까지 전주시 연간 강수량을 막대그래프로 그리시오
    


if __name__ == "__main__":
    main()