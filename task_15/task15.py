import requests
import os.path

def read_weather(weather_filename, col_idx, conv = float):
    dataset = []
    with open(weather_filename) as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            dataset.append(conv(tokens[col_idx]))
    return dataset

def rainfall_over_5mm(rainfalls):
    rainfall_over = []
    for rainfall in rainfalls:
        if rainfall > 5:
            rainfall_over.append(rainfall)
    return rainfall_over

def main():
    year = 2023
    URL = f"https://api.taegon.kr/stations/146/?sy={year}&ey={year}&format=csv"

    filename = f"weather_{year}.csv"

    if not os.path.exists(filename):
        resp = requests.get(URL)
        with open(filename,"w", encoding="UTF-8-sig") as fout:
            fout.write(resp.text)
    else:
        print(f"이미 {filename}이 있습니다.")


    weather_filename = "weather_2023.csv"
    tavg = read_weather(weather_filename, 4)
    rainfalls = read_weather(weather_filename, 9)
    rainfall_over5 = rainfall_over_5mm(rainfalls)


    print(sum(tavg)/len(tavg))
# "1, 연 평균 기온(일평균 기온의 연평균)"

    print(len(rainfall_over5))
# "2, 5mm 이상 강우일수"

    print(sum(rainfalls))
# "3, 이게 총 강우일수"

if __name__ == '__main__':
    main()