nums = input("숫자를 입력하시오")

# print(nums)

def average(nums):
    input_text = nums
    numbers = []
    for number in input_text.split():
        numbers.append(int(number))
    return sum(numbers) / len(numbers)

def main():
    print(average(nums))
    print(f"당신이 입력한 숫자들의 평균은 {average(nums)}입니다.")

if __name__ == "__main__":
    main()