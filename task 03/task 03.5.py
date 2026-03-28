#5) 두 지점 사이 거리 구하기
import math
x1 = int(input("x1을 입력하시오"))
y1 = int(input("y1을 입력하시오"))
x2 = int(input("x2을 입력하시오"))
y2 = int(input("y2을 입력하시오"))
distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)
print(distance)
print(f"점의 좌표가({x1},{y1})인 점에서 부터 ({x2},{y2})인 점까지의 거리는 {distance}입니다.")
