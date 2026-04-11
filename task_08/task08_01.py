cal_dict = {
    "한라봉": 30, "딸기": 34, "바나나": 77, "사과": 60, "배": 55
}
eat_dict = {
    "한라봉": 200, "매플망고": 300
}

def T_cal(cal_dict, eat_dict):
    total_cal = 0
    for key, val in eat_dict.items():
        if key in cal_dict:
            total_cal += val * cal_dict[key]
        else:
            cal = int(input(f"{key}의 칼로리를 입력하시오"))
            total_cal += cal * eat_dict[key]
    return total_cal

def main():
    # print(T_cal(cal_dict, eat_dict))
    print("총 칼로리는 {:,}(kcal)입니다.".format(T_cal(cal_dict, eat_dict)))

if __name__ == "__main__":
    main()