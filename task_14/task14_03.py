def read_dates(weather_filename):
    dates = []
    with open(weather_filename) as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            date = [int(tokens[0]), int(tokens[1]), int(tokens[2])]
            dates.append(date)
    # print(dates)
    return dates

def read_weather_col(weather_filename, col_idx):
    values = []
    with open(weather_filename) as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            value = float(tokens[col_idx])
            values.append(value)
    return values

def find_gdd200_dates(set_temp, set_date, dates,tavg):
    year = sorted(set(d[0] for d in dates))
    for year in year:
        gdd = 0
        gdd_found = False
        for i in range(len(dates)):
            d = dates[i]
            # print("i=", i, "d=", d)
            if d[0] == year and (d[1] > set_date[0] or (d[1] == set_date[0] and d[2] >= set_date[1])):
                t = tavg[i]
                if t >= set_temp:
                    gdd += (t-set_temp)
                if gdd > 200:
                    print(f'{year}년 {d[1]}월 {d[2]}일 누적적산온도: {gdd:.1f}도')
                    gdd_found = True
                    break
        if not gdd_found:
            print(f'{year}년 누적적산온도가 200도를 넘지 못했습니다.')


def main():
    weather_filename = "weather(146)_2001-2022.csv"
    dates = read_dates(weather_filename)
    tavg = read_weather_col(weather_filename, 4)
    # print(tavg)
    find_gdd200_dates(0, (4,15), dates, tavg)

if __name__=="__main__":
    main()