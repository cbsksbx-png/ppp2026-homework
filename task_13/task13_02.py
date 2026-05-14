def read_weather_col(weather_filename, col_idx, conv = float):
    dataset = []
    with open(weather_filename) as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            dataset.append(conv(tokens[col_idx]))
    return dataset

def sumifs(rainfalls, years, selected_years):
    total_value = 0
    for i in range(len(rainfalls)):
        r = rainfalls[i]
        y = years[i]
        if y in selected_years:
            total_value += r
    return total_value

def sum_annual(rainfalls, years):
    dataset = {}
    for y in years:
        dataset[y] = sumifs(rainfalls, years, [y])
    return dataset

# def N_years_rainfall(rainfalls, years, y):
#     for y in range(2001, 2023):
#         rainfall_y = sumifs(rainfalls, years, [y])
#     return

def main():
    weather_filename = "weather(146)_2001-2022.csv"
    rainfall = read_weather_col(weather_filename, 9)
    years = read_weather_col(weather_filename, 0, int)

    rainfall_2021 = sumifs(rainfall, years, [2021])
    rainfall_2022 = sumifs(rainfall, years, [2022])
    print(f"2021년 강수량은 {rainfall_2021:.1f}")
    print(f"2022년 강수량은 {rainfall_2022:.1f}")


if __name__ == '__main__':
    main()