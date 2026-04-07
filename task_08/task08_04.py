n = int(input("몇까지 더할지 입력하시오"))

def sum_n(n):
    total = 0
    for i in range(0 , n+1):
        total += i
    return total


def main():
    print(sum_n(n))

if __name__ == "__main__":
    main()