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
    years = sorted(set(d[0] for d in dates))
    for year in years:
        max_temp_gap = -999
        max_temp_gap_date = False
        max_temp_gap_day = []
        for i in range(len(dates)):
            d = dates[i]
            if d[0] == year:
                t = tmax[i] - tmin[i]
                if t > max_temp_gap:
                    max_temp_gap = t
                    max_temp_gap_day = d
                if d[1] == 12 and d[2] == 31:
                    # 이 조건 문만 만들면 끝남
                # print(max_temp_gap)  >> 하면 매년 12월 31일은 그해의 최고 온도차이
                    print(f"{year}년 {max_temp_gap_day[1]}월 {max_temp_gap_day[2]}일의 온도차이가 {max_temp_gap:.1f}으로 가장큽니다.")
                    max_temp_gap_date = True
                    break
        if not max_temp_gap_date:
            print("오류가 있습니다.")
                # print(d, t) >> 날짜 , 온도차이 출력 "완"
            # print(t_list)
                # print(t_list) >> 년도별로 온도차를 t_list 에 넣음,



                # if max_temp_gap == max(t_list):
                #     print(f"{year}년 {d[1]}월 {d[2]}일의 온도차이가 {max_temp_gap}으로 가장큽니다.")
                #     max_temp_gap_date = True
                #     break

        # print(f"{year}년 {d[1]}월 {d[2]}일의 온도차이가 {max_temp_gap}으로 가장큽니다.")
        # print(max_temp_gap)


            # print(t_gap) > 온도차이 파일은 만듬
            # print(f"{year}년 {d[1]}월 {d[2]}일의 온도차이가 {max_temp_gap}으로 가장큽니다.")


# 함수의 이름은 "maximum_tamp_gap"이고
# 함수의 매개변수는 3개 dates, tmax, tmin / 이들의 타입은 dates는 [2022,1,1] 같은 리스트가 모인 통 , tmax 랑 tmin 은 값들이 모인 통
# 함수의 리턴값은 2개 max_gap_date, max_gap / 이들의 타임은 max_gap_date 는 gap 이 가장 클때의 i에 대응하는 dates[i] 값 즉 리스트형태의 날짜, max_gap 은 [i]일때의 tmax - tmin 값


def main():
    weather_filename = "weather(146)_2001-2022.csv"
    dates = read_dates(weather_filename)
    tmax = read_weather_col(weather_filename, 3)
    tmin = read_weather_col(weather_filename, 5)
    # date, temp_diff = maximum_temp_gap(dates, tmax, tmin)
    # print(f"{date[0]}년 일교차가 가장 큰 날: {date}")
    # print(f"{date[0]}년 일교차가 가장 큰 날의 일교차는 {temp_diff:.1f}도")
    # 교수님 혹시 최고 일교차가 겹치면 함수값은 어떻게 나타내지나요?
    maximum_temp_gap(dates, tmax, tmin)

if __name__ == '__main__':
    main()

