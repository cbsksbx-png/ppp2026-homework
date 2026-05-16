def read_weather_col(weather_filename, col_idx):
    values = []
    with open(weather_filename) as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            value = float(tokens[col_idx])
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

def gdd_season(dates, tavg, abc = float, selected_month = [5,6,7,8,9], value = 2000):
    gdd_value = 0
    for i in range(len(dates)):
        date = dates[i]
        t = tavg[i]
        if date[1] in selected_month:
            gdd_value += abc(t - 5)
    if gdd_value > value:
        gdd_result = ("넘습니다.")
    else:
        gdd_result = ("넘지 못합니다.")
    return date[0] , gdd_value, selected_month, value, gdd_result

# def filter_month(tavg, dates, selected_months = [5,6,7,8,9]):
#     for dates[1] in selected_months:
#
#     return
#
# def gdd():
#
#     gdd_value = 0
#
#     return

def main():
    weather_filename = "weather(146)_2022-2022.csv"
    dates = read_dates(weather_filename)
    tavg = read_weather_col(weather_filename, 4)
    gdd_value = gdd_season(dates, tavg)
    print(f"{gdd_value[0]}년 {gdd_value[2]}월 GDD는 {gdd_value[1]}이고.")
    print(f"gdd는 {gdd_value[3]}을 {gdd_value[4]}")


if __name__ == '__main__':
    main()