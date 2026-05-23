def str2int(text:str):
    try:
        return int(text)
    except ValueError:
        return None

def main():
    values = []
    while True:
        x = input("X=> ?")
        x_value = str2int(x)
        if x_value == -1:
            break
        if x_value is not None:
            if x_value > 0 and type(x_value) == int:
                values.append(x_value)

    print(values)

    print(f"입력한 양수의 개수는 {len(values)}입니다.")
    print(f"입력한 양수의 평균은{sum(values)/len(values)}입니다.")

if __name__ == '__main__':
    main()