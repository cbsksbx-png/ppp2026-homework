y = int(input("확인할 년도를 입력하시오"))

def is_leap_year(y):
    if y % 4 == 0 and y % 100 != 0:
        print(f"{y}년은 윤년입니다.")
    else:
        print(f"{y}년은 윤년이 아닙니다.")

def main():
    is_leap_year(y)

if __name__ == "__main__":
    main()