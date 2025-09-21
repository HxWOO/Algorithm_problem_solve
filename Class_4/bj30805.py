import sys

N = int(sys.stdin.readline().rstrip())
A = list(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline().rstrip())
B = list(map(int, sys.stdin.readline().split()))

def solve(arr1: list, arr2: list):
    result = []

    while arr1 and arr2:
        max_arr1 = max(arr1)
        max_arr1_idx = arr1.index(max_arr1)

        max_arr2 = max(arr2)
        max_arr2_idx = arr2.index(max_arr2)

        if max_arr1 == max_arr2:
            result.append(max_arr1)
            arr1 = arr1[max_arr1_idx+1:]
            arr2 = arr2[max_arr2_idx+1:]
        elif max_arr1 > max_arr2:
            arr1.pop(max_arr1_idx)
        else:
            arr2.pop(max_arr2_idx)
    
    return result
    
answer = solve(A, B)
print(len(answer))
print(*answer)