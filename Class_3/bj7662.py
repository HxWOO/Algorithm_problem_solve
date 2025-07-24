import sys
import heapq


t = int(sys.stdin.readline())

for _ in range(t):
    k = int(sys.stdin.readline())
    min_heap, max_heap = [], []
    counts = dict()

    for _ in range(k):
        op, n_str = sys.stdin.readline().split()
        n = int(n_str)

        if op == 'I':
            heapq.heappush(min_heap, n)
            heapq.heappush(max_heap, -n)
            counts[n] = counts.get(n, 0) + 1
        
        elif n == 1: # 최댓값 삭제
            # 먼저 유령 데이터들을 모두 제거
            while max_heap and counts.get(-max_heap[0], 0) == 0:
                heapq.heappop(max_heap)
            
            if max_heap:
                removed = -heapq.heappop(max_heap)
                counts[removed] -= 1
        
        else: # 최솟값 삭제
            # 먼저 유령 데이터들을 모두 제거
            while min_heap and counts.get(min_heap[0], 0) == 0:
                heapq.heappop(min_heap)
            if min_heap:
                removed = heapq.heappop(min_heap)
                counts[removed] -= 1
                
    # 모든 연산 후, 최종적으로 힙에 남은 유령 데이터들을 정리
    while max_heap and counts.get(-max_heap[0], 0) == 0:
        heapq.heappop(max_heap)
    while min_heap and counts.get(min_heap[0], 0) == 0:
        heapq.heappop(min_heap)
        
    if not max_heap or not min_heap:
        print("EMPTY")
    else:
        print(-max_heap[0], min_heap[0])
