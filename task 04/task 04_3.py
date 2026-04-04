#3) 원의 둘레와 면적을 출력하는 프로그램
#3) 원의 면적, input 이용, math 이용
import math
r = int(input("원의 반지름을 입력하시오"))
area = round((math.pi * r**2), 2)
perimeter = round((math.pi * r), 1)
print(f"원의 면적은 {area}㎠이고 둘레는{perimeter}㎠입니다.")
print("원의 면적은 {}㎠이고 둘레는{}㎠입니다.".format(area, perimeter))
