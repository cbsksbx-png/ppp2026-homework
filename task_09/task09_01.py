nums = (10, 20, 30, 40, 50)
# 숫자 리스트를 (10, 20, 30, 40, 50) 이라고 했을때

def average(nums):
    return sum(nums) / len(nums)

def main():
    print(average(nums))

if __name__ == "__main__":
    main()