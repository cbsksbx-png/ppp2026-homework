# #2) BMI를 구하기 (input 이용, math 이용)
import math
weight = float(input("몸무게를 입력하시오"))
height = float(input("키를 입력하시오"))
# weight = 85
# height = 170
height_m = height/100
BMI = (weight/(height_m**2)//1)
print(BMI)
print(f"당신의 키가 {height}㎝이고 몸무게가 {weight}㎏일때 당신의 BMI지수는 {BMI}입니다.")
print("당신의 키가 {}㎝이고 몸무게가 {}㎏일때 당신의 BMI지수는 {}입니다".format(height,weight,BMI))
