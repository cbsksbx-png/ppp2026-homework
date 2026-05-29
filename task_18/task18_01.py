def toggle_text(text:str):
    result = ""
    # result += (f"{text}")
    for i in text:
        # result += i
        result += toggle_ch(i)
    return result

def toggle_ch(text):
    if ord(text) >= 65 and ord(text) <= 90:
        alphabet = chr(ord(text) + 32)
        return alphabet
    elif ord(text) >= 97 and ord(text) <= 122:
        alphabet = chr(ord(text) - 32)
        return alphabet
    else:
        return text
# 기존 결과로 하면 알파벳이 아닌 특정문자 ( !@# 등 ) 은 변환을 못해서 오류가 남

def main():
    print("정답")
    print(toggle_ch("a"))
    print(toggle_text("Hello, World"))
#     (hELLO, wORLD)

if __name__ == "__main__" :
    main()
