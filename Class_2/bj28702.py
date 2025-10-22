import sys


def print_fizzbuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0 and num % 5 != 0:
        print("Fizz")
    elif num % 3 != 0 and num % 5 == 0:
        print("Buzz")
    else:
        print(num)


first = sys.stdin.readline().rstrip()
second = sys.stdin.readline().rstrip()
third = sys.stdin.readline().rstrip()

nums = []
nums.append(first)
nums.append(second)
nums.append(third)
answer_num = 0

# 무조건 i 출력이 포함됨
for i in range(3):
    if nums[i].isnumeric():
        answer_num = int(nums[i])+(3-i)
        print_fizzbuzz(answer_num)
        exit()