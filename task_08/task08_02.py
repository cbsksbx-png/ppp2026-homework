dan = int(input("몇단인지 입력하시오"))

def gugudan(dan):
    for n in range(1, 10):
         print(f"{dan} X {n} = {dan * n}")

    # return ggd

# def gugudan(dan):
#     for n in range(1, 10):
#         return(f"{dan} X {n} = {dan * n}" )

def main():
    gugudan(dan)


if __name__ == "__main__":
    main()