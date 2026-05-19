def read_weather_col(weather_filename, col_idx = 9, conv_fn=float):
    datasets = []
    with open(weather_filename) as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            datasets.append(conv_fn(tokens[col_idx]))
    return datasets

def sumifs(rainfall, months, selected=[6,7,8]):
    total_value = 0
    for i in range(len(rainfall)):
        r = rainfall[i]
        m = months[i]
        if m in selected:
            total_value += r
    return total_value


def main():
    weather_filename = "weather(146)_2022-2022.csv"
    rainfall = read_weather_col(weather_filename)
    months = read_weather_col(weather_filename, 1, int)
    summer_rainfall = sumifs(rainfall, months)
    print(summer_rainfall)
    print(f"여름철 강수량은 {summer_rainfall:.1f}입니다.")


if __name__ == '__main__':
    main()