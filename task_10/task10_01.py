def text2list(list_text):
    input_text = list_text
    numbers = []
    for number in input_text.split():
        numbers.append(int(number))
    return numbers

def text_average(nums):
    return sum(nums) / len(nums)

def text_len(nums):
    return len(nums)

def text_max(nums):
    nums.sort(reverse=True)
    # print(nums)
    return nums[0]

def text_min(nums):
    nums.sort(reverse=False)
    return nums[0]

def text_median(nums):
    nums.sort(reverse=False)
    n = int(len(nums) / 2 + 0.5)
    if n % 2 == 0:
        return nums[n]
    else:
        return "없습니다."


def read_text(filename):
    with open(filename) as f :
        text = f.readline()
        # print(f"!{text}!")
    return text

def main():
    list_text = read_text("numbers1.txt")
    nums = text2list(list_text)
    print(nums)
    print("주어진 리스트는",nums)
    print("평균값은 {:.1f}".format(text_average(nums)))
    print("중앙값은 {}".format(text_median(nums)))
    print("주어진 숫자의 총개수 {}입니다.".format(text_len(nums)))
    print("주어진 숫자의 최대값 {}입니다.".format(text_max(nums)))
    print("주어진 숫자의 최솟값 {}입니다.".format(text_min(nums)))

if __name__=="__main__":
    main()