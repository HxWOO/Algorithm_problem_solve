# Python_problem_solve

- 파이썬으로 문제 해결
- solved.ac 의 클래스를 기준으로 점점 단계를 높여감
- -b, -s, -g 같은 식으로 푼 문제의 등급을 표시함


---

### 파라메트릭 서치

최적화 문제를 결정 문제(Yes or No)로 바꾸어 해결하는 기법
특정 조건 만족하는 가장 알맞은 값을 빠르게 찾는 최적화 문제에 사용됨
- Binary search

---
### 에라토스테네스의 체
- 소수를 구하는 방법
- 숫자 n까지의 소수를 구하려면 소수 m (m <= n^1/2)의 배수를 모두 빼는식으로 체로 불순물을 거르듯이 걸러냄

---
### 유클리드 호제법
- 2개의 자연수의 최대공약수를 구하는 알고리즘
- 두 자연수 a, b 에 대해 a를 b로 나눈 나머지인 r이라 하면, a와 b의 최대공약수는 b와 r의 최대공약수와 같다.
- 따라서, 이 과정을 최대공약수가 나올때까지 재귀적으로 반복하면 최대공약수를 구할 수 있다.
- e.g. "클래스2 2609번"

---
### 입력
- 파이썬의 sys 라이브러리의 sys.stdin.readline() 메서드 사용하면 입력 받는 시간을 input()을 쓸 때 보다 크게 줄일 수 있음

---
### 다이내믹 프로그래밍
- 최적화 인론의 한 기술, 특정 범위까지의 값을 구하기 위해 그것과 다른 범위까지의 값을 이용하여 효율적으로 구하는 알고리즘
- 이전에 풀었던 답을 재활용, 답을 구하기 위해서 했던 계산을 또 해야하는 종류의 최적 부분 구조 문제에서 효율적임

---
### 2차원 배열
- 파이썬에서 2차원 배열 선언 
- ```python
    dp = [[0 for i in range(15)] for 0 in range(15)]
---
### Deque
- 보통의 큐는 선입선출, 덱은 양방향 큐임
- 일반적인 리스트와 다르게 덱은 양끝 엘리먼트에 대해 append, pop이 압도적으로 빠름 O(1)
- ```python
  from collections import  # 이렇게 import 해서 사용
  
  deq = deque()  # 선언
- 덱의 메서드들
- append, appendleft, pop, popleft, extend, extendleft, rotate
- rotate : 양수, 음수 값을 파라미터로 넣어서 좌, 우로 회전 가능
---
### round 함수
- 파이썬에서 반올림 함수인 round() 함수는 일반적인 반올림 기법과 다르게 오사오입 기법임
- 오사오입: 앞자리 정수가 짝수면 5에서 버리고, 홀수면 5에서 올림
- math.ceil(): 올림, math.floor(): 내림 / 두 함수를 적절히 이용해서 사사오입하는 함수를 만들 수 있음

---
### 파이썬의 재귀
- 파이썬의 재귀 limit는 1000으로 매우 작기 때문에
- ```python 
  sys.setrecursionlimit()
- 를 이용해 재귀 깊이를 늘려줘야 함
---
### DFS

- DFS란 Depth first search의 약자로서 그래프 자료에서 데이터를 탐색하는 알고리즘입니다.
- 항상 "앞으로 찾아 가야할 노드"와 "이미 방문한 노드"를 기준으로 데이터를 탐색
- 스택/큐 or 재귀함수 활용 가능
- ```python 
  def dfs2(graph, start_node):
    ## deque 패키지 불러오기
    from collections import deque
    visited = []
    need_visited = deque()
    
    ##시작 노드 설정해주기
    need_visited.append(start_node)
    
    ## 방문이 필요한 리스트가 아직 존재한다면
    while need_visited:
        ## 시작 노드를 지정하고
        node = need_visited.pop()
 
        ##만약 방문한 리스트에 없다면
        if node not in visited:
 
            ## 방문 리스트에 노드를 추가
            visited.append(node)
            ## 인접 노드들을 방문 예정 리스트에 추가
            need_visited.extend(graph[node])
                
    return visited
---
### 분할 정복 (Divide and Conquer)
- 엄청나게 크고 방대한 문제를 조금씩 조금씩 나눠가면서 용이하게 풀 수 있는 문제 단위로 나눈 다음 그것들을 다시 합쳐서 해결하자는 개념
- 분할 정복법은 재귀적으로 자신을 호출하면서 그 연산의 단위를 조금씩 줄어가는 방식
- ```
  function F(x):
      if F(x)가 간단 then:
          return F(x)를 계산한 값
      else:
          x 를 x1, x2로 분할
          F(x1)과 F(x2)를 호출
          return F(x1), F(x2)로 F(x)를 구한 값
- 장점
  - 문제를 나눔으로써 어려운 문제를 해결할 수 있다
  - 병렬적으로 문제를 해결하는 데 큰 강점
- 단점
  - 함수를 재귀적으로 호출한다는 점에서 함수 호출로 인한 오버헤드가 발생
  - 스택 오버플로우가 발생하거나 과도한 메모리 사용을 하게 됨
  - "F(x)가 간단하다"라는 것을 정의하는 것이 난해함
---