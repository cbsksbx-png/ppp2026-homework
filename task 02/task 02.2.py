#2) 키와 몸무게가 임의로 주어졌을 때 BMI를 구하시오
weight = 60
height = 170
BMI = (weight/(height*0.01)**2)
print(BMI)
print(f"당신의 키가 {height}㎝이고 몸무게가 {weight}㎏일때 당신의 BMI지수는 {BMI}입니다.")
print("당신의 키가 {}㎝이고 몸무게가 {}㎏일때 당신의 BMI지수는 {}입니다".format(height,weight,BMI))
