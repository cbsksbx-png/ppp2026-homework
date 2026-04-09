nums = input("숫자를 입력하시오")

def average(nums):
    input_text = nums
    tokens = input_text.split()
    numbers = []
    for token in tokens:
        numbers.append(int(token))
    return sum(numbers) / len(numbers)

def main():
    print(average(nums))

if __name__ == "__main__":
    main()