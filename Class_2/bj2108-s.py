from functools import cmp_to_key


def cmp(tup_a, tup_b):
    if tup_a[1] > tup_b[1]:
        return 1
    elif tup_a[1] < tup_b[1]:
        return -1
    else:
        if tup_a[0] > tup_b[0]:
            return -1
        else:
            return 1


n = int(input())
nums = []

for i in range(n):
    nums.append(int(input()))

freq_list = []
for num in nums:
    cnt = nums.count(num)
    freq_list.append((num, cnt))

freq_list.sort(key=cmp_to_key(cmp))

new_freq_list = []
for freq in freq_list:
    if freq not in new_freq_list:
        new_freq_list.append(freq)  # 숫자, 숫자가 나온 횟수를 튜플로 저장

print(sum(nums)//len(nums))  # 산술 평균
print(sorted(nums).__getitem__((n+1)//2 - 1))  # 중앙값
try:
    if new_freq_list[-1][1] == new_freq_list[-2][1]:  # 최빈값, 여러개이면 두번째로 작은거 출력
        print(new_freq_list[-2][0])
    else:
        print(new_freq_list[-1][0])

except:  # 최빈값 리스트에 하나만 들어있을 경우
    print(new_freq_list[-1][0])

print(max(nums)-min(nums))  # 범위
