import sys                  # 빠른 입력을 위해 sys 모듈 사용
import bisect               # 이분 탐색(bisect_left)으로 O(log N) 위치 탐색
input = sys.stdin.readline  # 입력 속도 최적화

N = int(input().rstrip())   # 수열의 길이 N (1 ≤ N ≤ 1000)
A = list(map(int, input().split()))  # 수열 A (원소 1 ≤ Ai ≤ 1000)

def get_LIS_length_per_index(arr):
    """
    arr의 각 인덱스 i에 대해,
    'arr[i]로 끝나는 (strict) 증가 부분 수열의 길이'를 O(N log N)으로 구해 dp에 담아 반환.
    핵심 아이디어: 'tails(lis) 배열' 유지 + bisect_left 로 위치 탐색.
    lis[L] = '길이가 L+1인 증가 부분 수열'의 가능한 '최소 끝값'을 유지.
    """
    n = len(arr)
    dp = [0] * n            # dp[i] := arr[i]로 '끝나는' 증가 부분 수열의 길이
    lis = []                # tails 역할. 길이가 k인 LIS의 '최소 끝값'을 lis[k-1]에 저장

    for i in range(n):                  # 왼쪽에서 오른쪽으로 순차 처리
        x = arr[i]                      # 현재 원소
        pos = bisect.bisect_left(lis, x)
        # pos = lis에서 x를 끼워 넣을 가장 왼쪽 위치(첫 위치)
        # - strict 증가(LIS) 유지: 같거나 큰 값이 있는 맨 앞에 덮어씀
        # - non-decreasing(비내림)이라면 bisect_right를 사용

        if pos == len(lis):
            lis.append(x)               # x가 가장 큼 → LIS 길이 1 증가
        else:
            lis[pos] = x                # 길이 pos+1짜리 수열의 '최소 끝값'을 더 작게 갱신

        dp[i] = pos + 1                 # x를 끝값으로 하는 LIS 길이는 (0-index → +1)

    return dp

# 1) 왼쪽→오른쪽으로 'i에서 끝나는 증가 부분 수열 길이'
LIS = get_LIS_length_per_index(A)

# 2) 오른쪽→왼쪽으로 'i에서 시작하는 감소 부분 수열 길이'를 얻고 싶다.
#    감소(LDS)는, 배열을 뒤집어서 '증가 LIS'를 구한 뒤 다시 뒤집으면 된다.
#    (원본에서 i 이후로 '내림차순'인 수열 ↔ 뒤집힌 배열에서는 '오름차순' 수열)
LDS_reversed = get_LIS_length_per_index(A[::-1])  # 뒤집힌 배열에서 '끝나는 LIS 길이'
LDS = LDS_reversed[::-1]                          # 다시 원래 인덱스 순서로 뒤집어서 정렬

# 3) 각 i를 '꼭짓점'으로 하는 바이토닉 길이 = LIS[i] + LDS[i] - 1
#    (i가 두 번 더해지므로 -1)
answer = max(LIS[i] + LDS[i] - 1 for i in range(N))

print(answer)                     # 가장 긴 바이토닉 부분 수열 길이