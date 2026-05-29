import random

def gugudan_correct():
    a = random.randint(2,9)
    b = random.randint(1,9)
    ans = input(f"{a} X {b} =>>?")
    return int(ans) == a*b

def gugudan_game():
    return

def main():
    while True:
        score = 0
        life = 3
        for i in range(10):
            if gugudan_correct():
                score += 10
            else:
                life -= 1
                print(f"틀리셨습니다. 남은 목숨은{life}개 입니다.")
                if life == 0:
                    print(f"게임 종류입니다. 점수는 {score}입니다.")
                    break
        print(f"총 점수는 {score}입니다.")
        break

if __name__ == '__main__':
    main()