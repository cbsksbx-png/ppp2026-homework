#5-1) "화씨->섭씨", "섭씨->화씨", "피트(ft)->cm", "cm->피트(ft)" 변환을 선택하도록 하고, 기능 선택 후 변환 프로그램
start = input("℃, ℉, ft, cm 중 입력할 단위를 선책하시오")

if start == "℃" :
    C = float(input("몇 섭씨를 화씨로 바꾸겠습니까?"))
    F = round(C * 1.8 + 32, 1)
    print(f"당신이 입력한 {C}℃는 {F}℉입니다. ")

    if F > 212 :
        print("물이 끓는점보다 높습니다.")
    elif F < 32 :
        print("물이 어는점보다 낮습니다.")
    else :
        print(f"온도는 {F}℉입니다.")

if start == "℉" :
    F = float(input("몇 화씨를 섭씨로 바꾸겠습니까?"))
    C = ((F - 32) / 1.8, 1)
    print(f"당신이 입력한 {F}℉는 {C}℃입니다. ")

    if C > 100 :
        print("물이 끓는점보다 높습니다.")
    elif C < 0 :
        print("물이 어는점보다 낮습니다.")
    else :
        print(f"온도는 {C}℃입니다.")

if start == "ft" :
    FT = int(input("몇 피트를 cm로 변환하시겠습니까?"))
    CM = round(FT * 30.48, 1)
    print(f"당신이 입력한 {FT}ft는 {CM}cm입니다.")

if start == "cm" :
    CM = int(input("몇 cm를 피트로 변환하시겠습니까?"))
    FT = round(CM / 30.48, 1)
    print(f"당신이 입력한 {CM}cm은 {FT}ft입니다.")