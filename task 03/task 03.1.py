#1) 섭씨를 화씨로 변환하는 프로그램 (input 이용)
temp_c = float(input("온도를 입력하시오 =>"))
# temp_c = 50
temp_f = temp_c*9/5+32
print(temp_f)
print(f"{temp_c}℃ => {temp_f}℉")