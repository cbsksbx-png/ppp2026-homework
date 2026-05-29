def caesar_e(text:str, shift:int = 3):
    if ord(text) >= 65 and ord(text) <= (90 - shift) or ord(text) >= 97 and ord(text) <= (122 - shift):
        alphabet = chr(ord(text) + shift)
        return alphabet
    elif ord(text) >= (90 - shift) and ord(text) <= 90 or ord(text) <= 122 and ord(text) >= (122 - shift) :
        alphabet = chr(ord(text) + shift - 25)
        return alphabet
    else:
        return text

def caesar_encode(text:str, shift:int = 3):
    result = ""
    for i in text:
        result += caesar_e(i)
    return result

def caesar_d(text:str, shift:int = 3):
    if ord(text) >= (65 + shift) and ord(text) <= 90 or ord(text) >= (97 + shift) and ord(text) <= 122 :
        alphabet = chr(ord(text) - shift)
        return alphabet
    elif ord(text) >= 65 and ord(text) <= 65 + shift or ord(text) <= (97 + shift) and ord(text) >= 97 :
        alphabet = chr(ord(text) - shift - 25)
        return alphabet
    else:
        return text

def caesar_decode(text:str, shift:int = 3):
    result = ""
    for i in text:
        result += caesar_e(i)
    return result



def main():
    print(caesar_encode(input("문자를 입력하시오"), 3))
    print(caesar_decode(input("문자를 입력하시오"), 3))

if __name__ == "__main__" :
    main()