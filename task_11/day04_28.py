def calc_cal(eat_dict, calories_dict):
    total_cal = 0
    for key, val in eat_dict.items():
        if key in calories_dict:
            total_cal += calories_dict[key] * val
    return total_cal

def read_cal_db(filename):
    cal_dict = {}
    with open(filename, encoding="utf-8-sig") as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            fruit = tokens[0]
            cal = int(tokens[1])
            cal_dict[fruit] = cal
    return cal_dict

def main():
    calories_dict = read_cal_db("calorie_db.csv")
    eat_dict = {
        "밀" : 100
    }
    total_cal = calc_cal(eat_dict, calories_dict)
    print(f"총 칼로리는  {total_cal:.1f}입니다.")

if __name__ == "__main__":
    main()