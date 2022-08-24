# 큐의 특성
* 뒤에서는 삽입만, 앞에서는 삭제만하는 구조
* 선입선출구조 (FIFO) : 먼저 삽입된 원소는 가장 먼저 삭제

# 주요 연산
* enQueue(item) : 큐의 뒤쪽에 원소를 삽입
```python
def enQueue(item):
    global rear         # 마지막 원소의 인덱스를 글로벌 변수로 받아옴
    if isFull():        # 큐가 가득찼으면 출력
        print('Queue_Full')
    else:               # 공간이 있으면 인덱스를 하나 증가 시켜주고 item 삽입
        rear += 1
        Q[rear] = item
```
* deQueue() : 큐의 앞쪽에서 원소를 삭제하고 반환
```python
def deQueue():        
    if isEmpty():
        print('Queue_Empty')
    else:               # 원소가 있으면 front인덱스를 두번째꺼로 바꾼뒤 리턴
        front += 1
        return Q[front]
```
* createQueue() : 공백 큐를 생성
* isEmpty() : 큐가 공백상태인지 확인
```python
def isEmpty():
    return front == rear   
```
* isFull() : 큐가 포화상태인지 확인
```python
def isFull():
    return rear == len(Q)-1   
```
* Qpeek() : 큐의 앞쪽에서 원소를 삭제없이 반환
```python 
def Qpeek():
    global front
    if isEmpty():
        print('Queue_Empty')
    else:
        return Q[front+1]
```

# 선형 큐
* 1차원 배열을 이용한 큐 
* 큐의 크기 = 배열의 크기
* 초기 상태 : front = rear = -1
* 공백 상태 : front == rear
* 포화 상태 : rear == n-1(마지막 인덱스)
* 문제점
  * 잘못된 포화 상태 인식
    * 선형 큐에서 삽입, 삭제 반복시, 배열의 앞부분에 공간이 있음에도 불구하고 rear = n-1 이 되어 포화상태로 인식해 더 이상 삽입을 수행하지 않는 문제가 발생
    * 해결 1
      * 매 연산마다 원소들을 앞으로 이동 => 이동에 시간 소요, 효율성 급감
    * 해결 2
      * 원형 형태의 큐를 이룬다고 가정하고 사용

# 원형 큐
* 초기 공백 상태 : front = rear = 0
* front가 있는 자리는 항상 빈자리로 둠
* 삽입 위치 : rear = (rear + 1) mod n
```python
def enQueue(item):
    global rear
    if isFull():
        print('Queue_Full')
    else:
        rear = (rear + 1) % len(cQ)
        cQ[rear] = item
```
* 삭제 위치 : front = (front + 1) mod n
```python
def deQueue():
    global front
    if isEmpty():
        print('Queue_Empty')
    else:
        front = (front + 1) % len(cQ)
        return cQ[front]
```
* 공백 상태 : front == rear
``` python
def isEmpty():
    return front == rear
```
* 포화 상태 : rear의 다음 위치 == front
```python
def isFull():
    return (rear + 1) % len(cQ) == front
```

# 우선순위 큐 (Priority Queue)
* 우선순위 큐의 특성
  * 우선순위를 가진 항목들을 저장하는 큐
  * FIFO 순서가 아니라 우선순위가 높은 순서대로 먼저 나감
* 적용 : 시뮬레이션 시스템, 네트워크 트래픽 제어, 운영체제의 테스크 스케줄링
* 문제점 : 배열을 사용하기 때문에, 삽입이나 삭제 연산 발생 시 원소의 재배치 필요 => 소요 시간, 메모리 낭비 큼

# 버퍼 (Buffer)
* 데이터를 한 곳에서 다른 곳으로 전송하는 동안 일시적으로 데이터를 보관하는 메모리 영역
* 버퍼링 : 버퍼를 활용하는 방식 / 버퍼를 채우는 동작
* 입출력, 네트워크와 관련된 기능에서 이용
* 순서대로 입력 / 출력 / 전달 => 선입선출 방식의 자료구조인 큐 활용


# BFS ( Breadth First Search )
* 그래프 탐색 방법 : 깊이 우선 탐색(DFS) / 너비 우선 탐색(BFS)
* 탐색 시작점의 인접한 정점들을 차례로 방문한 후에, 방문했던 정점을 시작점으로 해서 다시 인접한 정점을 차례로 방문하는 방식

```python
def BFS(G, v):                # G : 그래프 / v : 시작점
    visited = [0] * (n+1)     # n : 정점 개수
    queue = []                # 큐 생성
    queue.append(v)

    while queue:
        t = queue.pop(0)
        if not visited[t]:     # 첫번째 원소가 방문되지 않은 곳이면 방문한 걸로 표시
            visited[t] = 1
            visit(t)
            for i in G[t]:
                if not visited[i]:
                    queue.append(i)
```