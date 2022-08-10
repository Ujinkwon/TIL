# 2차원 배열
* 세로길이(행의 개수), 가로길이(열의 개수) 필요
* arr = [list(map(int, input().split())) for _ in range(N)]
  * N = 3
  * 1 2 3 
  * 4 5 6
  * 7 8 9
* arr = [list(map(int, input())) for _ in range(N)]
  * N = 4
  * 1234
  * 5678
  * 9101112
  

i : 행 / j : 열
## 행 우선 순회
```python
for i in range(n):   
    for j in range(m): 
        arr[i][j]
```

## 열 우선 순회
```python
for j in range(n):
    for j in range(m):
        arr[j][i]
```

## 지그재그 순회
```python
for i in range(n):
    for j in range(m):
        arr[i][j + (m-1-2*j) * (i%2)]
```
## 4방향의 인접 배열 요소 탐색
```python
arr = [list(map(int, input().split())) for _ in range(N)]   # N*N 배열
di = [0, 0, -1, 1]   # 좌우
dj = [-1, 1, 0, 0]   # 상하
for i in range(1, N):
    for j in range(1, N):
        for k in range(4):
            ni = j + di[k]
            nj = i + dj[k]
            if 0 <= ni < N and 0 <= nj < N:
                print(arr[ni][nj])
```

## 전치 행렬
```python
arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for i in range(3):
    for j in range(3):
        if i < j:
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
```
## 부분집합
* 집합 원소 n개 => 공집합 포함 부분집합 수 2^n개
```python
bit = [0, 0, 0, 0]
for i in range(2):
    bit[0] = i
    for j in range(2):
        bit[1] = j
        for k in range(2):
            bit[2] = k
            for l in range(2):
                bit[3] = l
                print(bit)
```

## 비트 연산자
* 비트 연산자 
  * & : and
  * | : or
  * << : 비트 열을 왼쪽으로 이동
  * >> : 비트 열을 오른쪽으로 이동
* 1 << n : 원소가 n개일 때 모든 부분집합의 수 (2^n)
* i & (1 << j) : i의 j번째 비트가 1인지 검사

```python
# 부분집합 생성

arr = [1, 2, 3, 4, 5, 6]
lenght = len(arr)

for i in range(1<<n):       # 부분집합 개수
    for j in range(n):      # 원소의 수만큼 비트 비교
        if i & (1<<j):      # i의 j번 비트가 1이면
            print(arr[j], end=",")     # j번 원소 출력
    print()
print()
```

# 검색
* 저장돼 있는 자료 중 원하는 항목 찾는 작업

## 순차 검색
* 일렬로 되어 있는 자료를 순서대로 검색
* 알고리즘이 단순해 구현이 쉬움
* 검색 대상의 수가 많으면 수행 시간이 급격하게 증가 => 비효율적

### 정렬되어 있지 않은 경우
1. 첫 번째 원소부터 순서대로 검색 대상과 키 값이 같은 원소가 있는지 비교
2. 같은 원소를 찾으면 그 원소의 인덱스를 반환
3. 마지막까지 찾지 못하면 검색 실패
```python
def seq(a, n, key):
    i = 0
    while i < n and a[i] != key:
        i = i + 1
    if i < n:
        return i
    else:
        return -1
```

### 정렬되어 있는 경우
1. 오름차순으로 정렬된 상태에서 검색 시작한다고 가정
2. 순차적으로 검색하면서 비교하여, 원소의 키 값이 검색 대상의 키 값보다 크면 검색 종료
* 검색 실패를 반환하는 경우 평균 비교 횟수가 반으로 줄어듬
```python
def seq2(a, n, key):
    i = 0
    while i < n and a[i] < key:
        i = i + 1
    if i < n and a[i] == key:
        return i
    else:
        return -1
```

## 이진 검색
* 가운데 있는 항목의 키 값과 비교 후, 다음 검색 위치를 결정해 진행
* 자료가 정렬된 상태여야 함
1. 중앙에 있는 원소를 고른다.
2. 값을 비교한다.
3. 목표 값이 중앙 원소 값보다 작으면 왼쪽 반을 검색하고, 크면 오른쪽 반을 검색
4. 값을 찾을 때까지 반복
```python
def binarysearch(a, n, key):
    start = 0
    end = n - 1
    while start <= end:
        middle = (start + end) // 2
        if a[middle] == key:
            return True
        elif a[middle] > key:
            end = middle - 1
        else:
            start = middel + 1
    return False
```

## 선택 정렬
* 가장 작은 값의 원소부터 차례대로 위치를 교환하는 방법
1. 리스트에서 최소값을 찾는다.
2. 리스트의 맨 앞의 값과 교환
3. 맨 처음 위치 제외한 리스트로 반복

```python
def selectionsort(a, n):
    for i in range(n-1):
        minidx = i
        for j in range(i + 1, n):
            if a[minidx] > a[j]:
                minidx = j
        a[i], a[minidx] = a[minidx], a[i]
```
```python
# k번째로 작은 원소 찾기
def select(a, k):
    for i in range(k):
        minidx = i
        for j in range(i + 1, len(a)):
            if a[minidx] > a[j]:
                minidx = j
        a[i], a[minidx] = a[minidx], a[i]
    return a[k-1]
```
