def read_weather_col(weather_filename, col_idx, conv_fn = float):
    values = []
    with open(weather_filename) as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            value = conv_fn(tokens[col_idx])
            values.append(value)
    return values

def read_dates(weather_filename):
    dates = []
    with open(weather_filename) as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            date = [int(tokens[0]), int(tokens[1]),int(tokens[2])]
            dates.append(date)
    return dates

def gdd_season(dates, tavg, selected_month = [5,6,7,8,9], value = 5):
    year = sorted(set(d[0] for d in dates))
    for year in year:
        gdd_value = 0
        gdd_found = False
        for i in range(len(dates)):
            d = dates[i]
            # if d[0] == year and d[1] in selected_month:
            if d[0] == year and (d[1] >= selected_month[0] or (d[1] == selected_month[0] and d[2] >= 1)):
                # print(d)
                t = tavg[i]
                if t - value >= 0:
                    gdd_value += t - value
                if t - value < 0:
                    gdd_value += 0
                if d[1] == selected_month[-1] and d[2] == 30:
                    print(f"{year}년 적산온도는 {gdd_value}입니다.")
                    gdd_found = True
                    break
        if not gdd_found:
            print("gdd_value를 찾지 못했습니다.")

                    # print(f"{year}년 적산온도는 {gdd_value}입니다.")
                    # gdd_found = True
                    # break
                    # print(f"{year}년 {gdd_value}")

def main():
    weather_filename = "weather(146)_2001-2022.csv"
    dates = read_dates(weather_filename)
    tavg = read_weather_col(weather_filename, 4, )
    gdd_season(dates,tavg)




if __name__ == '__main__':
    main()