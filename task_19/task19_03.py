import random

def hangman(ran_word, trial):
    mas = 0
    initial = input("답을 입력하시오")
    word = ""
    for i in ran_word:
        if i == initial:
            word += i
            mas += 1
            print(f"{word}" + "_" * (len(ran_word) - mas))
            initial = input("답을 입력하시오")
            if word == ran_word:
                print("정답입니다.")
                break
        else:
            print(f"{word}" + "_" * (len(ran_word) - mas))
            trial -= 1
            print(f"틀렸습니다. 목숨은 {trial}개 입니다.")
            initial = input("답을 입력하시오")
            if i == initial:
                word += i
                mas += 1
                print(f"{word}" + "_" * (len(ran_word) - mas))
                initial = input("답을 입력하시오")
                if word == ran_word:
                    print("정답입니다.")
                    break
    return


def main():
    list = ["apple" , "banana" , "pineapple"]
    trial = 7
    # list는 단어모음 / trial은 목숨
    ran_word = random.choice(list)
    print("_" * len(ran_word), f"목숨 : {trial}")

    hangman(ran_word, trial)

# 고칠점있음 일단 먼저 banana를 완성을 해도 바로 정답을 안되침

if __name__ == '__main__':
    main()