#3) 원의 면적, input 이용, math 이용
import math
r = int(input("원의 반지름을 입력하시오"))
area1 = (math.pi * r**2)//1
print(area1)
print(f"원의 면적은 {area1}㎠입니다.")
print("원의 면적은 {}㎠입니다.".format(area1))