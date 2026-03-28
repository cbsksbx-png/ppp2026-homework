#2) x, y의 입력값을 받고 어느 사분인지 출력하기
import math
x1 = int(input("x1을 입력하시오"))
y1 = int(input("y1을 입력하시오"))
# x2 = int(input("x2을 입력하시오"))
# y2 = int(input("y2을 입력하시오"))
# distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)
# print(distance)
# print(f"점의 좌표가({x1},{y1})인 점에서 부터 ({x2},{y2})인 점까지의 거리는 {distance}입니다.")

if x1 > 0 and y1 > 0 :
    print(f"입력한 1번 점의 좌표는 ({x1},{y1})로 1사분면입니다.")
elif x1 > 0 and y1 < 0 :
    print(f"입력한 1번 점의 좌표는 ({x1},{y1})로 4사분면입니다.")
elif x1 < 0 and y1 > 0 :
    print(f"입력한 1번 점의 좌표는 ({x1},{y1})로 2사분면입니다.")
elif x1 < 0 and y1 < 0 :
    print(f"입력한 1번 점의 좌표는 ({x1},{y1})로 3사분면입니다.")
elif x1 == 0 and y1 == 0 :
    print("이점은 원점입니다.")
elif x1 == 0 :
    print("이점은 x축위에 있습니다.")
elif y1 == 0 :
    print("이점은 y축 위에 있습니다.")

