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

def maximum_temp_gap(dates, tmax, tmin):
    max_gap = -999
    max_gap_date = None

    for i in range(len(dates)):
        gap = tmax[i] - tmin[i]
        if gap > max_gap :
            max_gap = gap
            max_gap_date = dates[i]
    return max_gap_date, max_gap
# 함수의 이름은 "maximum_tamp_gap"이고
# 함수의 매개변수는 3개 dates, tmax, tmin / 이들의 타입은 dates는 [2022,1,1] 같은 리스트가 모인 통 , tmax 랑 tmin 은 값들이 모인 통
# 함수의 리턴값은 2개 max_gap_date, max_gap / 이들의 타임은 max_gap_date 는 gap 이 가장 클때의 i에 대응하는 dates[i] 값 즉 리스트형태의 날짜, max_gap 은 [i]일때의 tmax - tmin 값


def main():
    weather_filename = "weather(146)_2022-2022.csv"
    dates = read_dates(weather_filename)
    tmax = read_weather_col(weather_filename, 3)
    tmin = read_weather_col(weather_filename, 5)
    date, temp_diff = maximum_temp_gap(dates, tmax, tmin)
    print(f"일교차가 가장 큰 날: {date}")
    print(f"일교차가 가장 큰 날의 일교차는 {temp_diff:.1f}도")

if __name__ == '__main__':
    main()