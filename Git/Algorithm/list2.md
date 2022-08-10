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