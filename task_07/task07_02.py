mart = {"우유" : 2800 , "계란" : 300 , "빵" : 1200 , "물" : 1700}

cart = ["물" , "물" , "계란" , "빵" , "빵" , "바나나"]

total_cost = 0
for item in cart :
    if item in mart :
        total_cost += mart[item]
    else :
        cost = int(input(f"{item}가격을 입력하시오"))
        total_cost += cost

print(total_cost)
print("총 가격은 {:,}원 입니다.".format(total_cost))

# 7.2 과제는 가격을 입력하시오에 mart에 없는 물건의 이름을 .format로 넣고 싶음
# 두번째는 cart에 내가 원하는 물건을 넣는것