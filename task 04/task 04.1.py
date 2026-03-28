#1) BMI계산정도에 따라 비만 정도를 표시
import math
weight = float(input("몸무게를 입력하시오"))
height = float(input("키를 입력하시오"))
# weight = 85
# height = 170
height_m = height/100
BMI = round(weight/(height_m**2), 1)
print(BMI)
print(f"당신의 키가 {height}㎝이고 몸무게가 {weight}㎏일때 당신의 BMI지수는 {BMI}입니다.")
print("당신의 키가 {}㎝이고 몸무게가 {}㎏일때 당신의 BMI지수는 {}입니다".format(height,weight,BMI))

if 23 <= BMI < 25 :
    print(f"당신의 BMI지수는 {BMI}㎏/㎡로 당신은 비만 2020년 기준 비만 전단계입니다.")
elif 25 <= BMI < 30 :
    print(f"당신의 BMI지수는 {BMI}㎏/㎡로 당신은 비만 2020년 기준 1단계 비만입니다.")
elif 30 <= BMI < 35:
    print(f"당신의 BMI지수는 {BMI}㎏/㎡로 당신은 비만 2020년 기준 2단계 비만입니다.")
else :
    print(f"당신의 BMI지수는 {BMI}㎏/㎡로 당신은 비만 2020년 기준 3단계 비만입니다.")
