import random

def korean_to_be_initial(ran_word):
    CHOSUNG_LIST = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
    r_list = []
    for w in list(ran_word.strip()):
        if '가'<=w<='힣':
            ch1 = (ord(w) - ord('가')) // 588
            r_list.append(CHOSUNG_LIST[ch1])
        else:
            r_list.append([w])
    return r_list

# def word_list(word):
#     ran_word = random.choice(word)
#     return korean_to_be_initial(ran_word), ran_word


def main():
    word = [ "바나나", "사과", "귤" ]
    random_word = random.choice(word)
    ran_word_initial = korean_to_be_initial(random_word)
    # word_initial = word_list(word)[0]
    # r_word = word_list(word)[1]
    print(ran_word_initial)
    # print(r_word)
    # -> r_word 랑 word_initial 이랑 달라서 문제 발생
    while True:
        x = input("X=> ?")
        if x == random_word:
            print("정답입니다.")
            break
        else:
            print("틀렵습니다,")

if __name__ == "__main__":
    main()