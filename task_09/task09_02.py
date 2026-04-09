n = int(input("돌려받을 숫자의 최대값을 입력하시오"))

def get_range_list(n):
    list = []
    for i in range(0 , n+1):
        list.append("{}".format(i))
    return list

def main():
    print(get_range_list(n))

if __name__ == "__main__":
    main()