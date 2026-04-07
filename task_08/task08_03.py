t_c = int(input("섭씨를 입력하시오"))

def c2f(t_c):
    t_f = (t_c * 1.8) +32
    return(t_f)

def main():
    print(c2f(t_c))

if __name__=="__main__" :
    main()

