from collections import Counter
import sys
import math

n = int(sys.stdin.readline().rstrip())
nums = []

total_sum = 0
for i in range(n):
    num = int(sys.stdin.readline().rstrip())
    total_sum += num
    nums.append(num)

nums.sort()
print(round(total_sum/n))  # 산술 평균
print(nums[n//2])  # 중앙 값
counters = Counter(nums).most_common(2)
if n == 1:
    print(counters[0][0])
elif counters[0][1] == counters[1][1]:  # 최빈값
    print(counters[1][0])
else:
    print(counters[0][0])

print(nums[-1]-nums[0])  # 범위
