import random


def spitto():
    num_range = list(range(1, 46))
    lotto = []
    for i in range(6):
        r = random.choice(num_range)
        if r not in lotto:
            lotto.append(r)
        elif r in lotto:
            R = int(r)
            num_range.remove(R)
            x = random.choice(num_range)
            lotto.append(x)
    return lotto

def made_lotto(time):
    result = ""
    for i in range(int(time)):
        result += str(spitto()) + "\n"
    return result

def main():
    time = input("원하는 횟수를 입력하시오")
    lotto = spitto()
    # print(lotto)
    print(made_lotto(time))


if __name__ == "__main__":
    main()
