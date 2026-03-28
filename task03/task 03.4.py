#4) 사다리꼴 면적, input 3번 입력받기
bottom = int(input("밑변의 길이를 입력하시오"))
top = int(input("윗변의 길이를 입력하시오"))
height = int(input("높이를 입력하시오"))
area2 = (bottom+top) /2 * height
print(area2)
print(f"사다리꼴의 면적은 {area2}㎠ 입니다.")