def read_weather_col(filename, num_cols):
    dataset = []
    with open(filename) as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            dataset.append(float(tokens[num_cols]))
    return dataset


def read_rainfall(filename):
    dataset = []
    with open(filename) as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            dataset.append(float(tokens[9]))
    return dataset

def read_tmax(filename):
    dataset = []
    with open(filename) as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            dataset.append(float(tokens[4]))
    return dataset

def get_days_over_5mm(rainfall):
    count_5mm = 0
    for r in rainfall:
        if r >= 5 :
            count_5mm += 1
    return count_5mm
    print([1 for x in rainfall if x >= 5])
    return sum([1 for x in rainfall if x >= 5])

def get_rain_event_days(rainfall):
    #비가 오면 1, 아니면 0
    dataset_rainfall = []
    for r in rainfall:
        if r > 0 :
            dataset_rainfall.append(1)
        else:
            dataset_rainfall.append(0)
    # print(dataset_rainfall)

    dataset_rain_event = []
    for i in range(len(rainfall)):
        r = dataset_rainfall[i] # 0 or 1
        if r == 0:
            # print(dataset_rain_event)
            dataset_rain_event.append(0)
        else:
            if i == 0:
                dataset_rain_event.append(r)
            else:
                dataset_rain_event.append(dataset_rain_event[i-1]+1)
    return dataset_rain_event

def get_max_rainfall_event(rainfall):
    datasets = []
    rainfall_event = None
    for r in rainfall:
        if r > 0:
            if rainfall_event != None:
                rainfall_event.append(r)
            else:
                rainfall_event = [r]
        else:
            if rainfall_event != None:
                datasets.append(rainfall_event)
            rainfall_event = None
    # print(datasets)
    print(max([len(x) for x in datasets]))
    return max([sum(x) for x in datasets])

def get_top3(list_values):
    return sorted(list_values)[-3:]

def main():
    weather_filename = "weather(146)_2022-2022.csv"
    # rainfall = read_rainfall(weather_filename)
    rainfall = read_weather_col(weather_filename, 9)
    # print(rainfall)
    days_over_5mm = get_days_over_5mm(rainfall)
    print(f"강수량이 5mm이상인 날은 {days_over_5mm}일 입니다.")

    max_rainy_days = max(get_rain_event_days(rainfall))
    print(f"최장 연속 강수일수는 {max_rainy_days}일 입니다.")

    max_rainfall_event = get_max_rainfall_event(rainfall)
    print(f"최장 연속 강수일수는 {max_rainfall_event}일 입니다.")

    tmax = read_weather_col(weather_filename, 4)
    tmax = read_tmax(weather_filename)
    tmax_top3 = get_top3(tmax)
    print(f"tmax 최대값 3개는 {tmax_top3}")

if __name__ == "__main__":
    main()