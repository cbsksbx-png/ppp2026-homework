#6) 칼로리 구하기
apple = int(input("섭취한 사과의 g을 입력하시오"))
strawberry = int(input("섭취한 딸기(설향)의 g을 입력하시오"))
banana = int(input("섭취한 바나나의 g을 입력하시오"))
kcal = (apple * (52/100)) + (strawberry * (34/100)) + (banana * (77/100))
print(kcal)
print(f"당신이 사과를 {apple}g 먹고 딸기를 {strawberry}g 먹고 바나나를 {banana}g 먹으면 총 섭취한 칼로리는 {kcal}(kcal)이다.")