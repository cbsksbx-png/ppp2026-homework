cal_dict = {
    "한라봉" : 30 , "딸기" : 34 , "바나나" : 77 , "사과" : 60 , "배" : 55
}
eat_dict = { "한라봉" : 200 , "매플망고" : 300}

total_cal = 0
for key, val in eat_dict.items() :
    if key in cal_dict :
        total_cal += val * cal_dict[key]
    else :
        cal = int(input(f"{key}의 칼로리를 입력하시오"))
        total_cal += cal * eat_dict[key]
print(total_cal)
print("전체 칼로리는 {:,}입니다.".format(total_cal))

# 7.1 과제는 완성 하지만 보완할점 eat_dict에 내가 원하는 음식이랑 그램넣기가 어려움 해결해서 제출하기