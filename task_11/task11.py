def read_tavg(weather_filename):
    tavg_dataset = []
    with open(weather_filename) as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            tavg_dataset.append(float(tokens[4]))
    return tavg_dataset

def read_rainfall(weather_filename):
    rain_dataset = []
    with open(weather_filename) as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            rain_dataset.append(float(tokens[9]))
    return rain_dataset

def rainfall_over_5mm(rainfalls):
    rainfall_over = []
    for rainfall in rainfalls:
        if rainfall > 5 :
            rainfall_over.append(rainfall)
    return rainfall_over


def main():
    weather_filename = "weather(146)_2022-2022.csv"
    tavgs = read_tavg(weather_filename)
    print(f"연 평균온도는{sum(tavgs) / len(tavgs)}")

    rainfalls = read_rainfall(weather_filename)
    print(f"총 강수량은{sum(rainfalls)}")
    rainfall_over5 = rainfall_over_5mm(rainfalls)
    print(f"강수량이 5mm이상인 날은 {len(rainfall_over5)}일 입니다.")

if __name__ == "__main__":
    main()