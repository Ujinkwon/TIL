# 위상 정렬 (Topological Sort)
* 방향 그래프에서 간선으로 주어진 정점 간 `선후관계를 위배하지 않는 정렬`
* Directed Acyclic Graph에서만 정의
* 사이클 존재 => 위상 정렬에 모든 정점이 포함되지 않게 됨
  * 위상 정렬 후, 결과에 모든 정점 존재 안하면 => 사이클있는 그래프
* `구현`
  * 정점들의 indegree 정보를 담은 배열 저장
  * indegree가 0인 정점들을 큐에 저장
  * 큐에서 하나 pop해 위상 정렬
  * 정렬된 정점과 연결된 모든 정점의 indegree 배열 값 -1
  * indegree 값이 0이 되면 큐에 append
  * 큐가 빌 때까지 반복

# 서로소 집합 (Disjoint-sets)
* 서로소 or 상호배타 집합 : 서로 중복 포함된 원소가 없는 집합들
* 대표자 : 각 집합을 구분하는 집합에 속한 하나의 특정 멤버

## 연결 리스트 
* 같은 집합의 원소들은 하나의 연결리스트로 관리
* 맨 앞의 원소를 집합의 대표 원소로 삼음
* 각 원소는 집합의 대표원소를 가리키는 링크를 가짐

## 트리
* 하나의 집합을 하나의 트리로 표현
* 자식 노드가 부모 노드를 가리키고 대표자는 루트 노드

* 상호배타 집합 연산 
  * Make-Set(x) : 유일한 멤버 x를 포함하는 새로운 집합 생성
  * Find-Set(x) : x를 포함하는 집합을 찾는 연산
  * Union(x, y) : x와 y를 포함하는 두 집합을 통합하는 연산

```python
def make_set(x):
  p[x] = x   

def find_set(x):
  if x == p[x]:
    return x
  else:
    find_set(p[x])

def union(x, y):
  p[find_set(y)] = find_set(x)
```
* 연산의 효율을 높이는 방법
  * rank를 이용한 union
    * 자신을 루트로 하는 서브트리의 높이를 rank라는 이름으로 저장
    * 두 집합을 합칠 때 rank가 낮은 집합을 높은 집합에 붙임
  * path compression
    * find-set 과정에서 만나는 모든 노드들이 직접 루트를 가리키도록 포인터를 바꿔줌

```python
def make_set(x):
  p[x] = x   # 노드 x의 부모 저장
  rank[x] = 0   # 루트 노드가 x인 트리의 랭크 값 저장

def find_set(x):
  if x != p[x]:  # x가 루트가 아닌 경우
    p[x] = find_set(p[x])
  return p[x]

def union(x, y):
  link(find_set(x), find_set(y))

def link(x, y):
  if rank[x] > rank[y]:   # rank : 트리 높이
    p[y] = x
  else:
    p[x] = y
    if rank[x] == rank[y]:
      rank[y] += 1
```

# 최소 비용 신장 트리 (MST)
* 신장 트리 : n개의 정점으로 이뤄진 무방향 그래프에서 n개의 정점과 n-1개의 간선으로 이뤄진 트리
* 최소 신장 트리 : 무방향 가중치 그래프에서 신장 트리를 구성하는 간선들의 가중치 합이 최소인 신장 트리

# Prim 알고리즘
* 하나의 정점에서 연결된 간선들 중에 하나씩 선택하면서 MST를 만들어 가는 방식
* 우선 순위 큐로 구현
* `구현`
  * 임의 정점 하나 선택해서 최소 신장 트리에 추가
  * 해당 정점과 연결된 모든 간선을 우선순위 큐에 추가
  * 우선순위 큐에서 비용이 가장 작은 간선을 pop
    * 해당 간선이 최소 신장 트리에 포함된 두 정점을 연결한다면, continue
    * 최소 신장 트리에 포함된 정점과 포함되지 않은 정점을 연결한다면, 
      * 해당 간선과 포함되지 않는 정점을 최소 신장 트리에 추가
      * 포함되지 않는 정점과 최소 신장 트리에 포함되지 않은 정점을 연결하는 모든 간선을 우선순위 큐에 추가
  * 최소 신장 트리에 v-1개의 간선이 추가 될 때 까지 반복
* 서로소인 2개의 집합 정보 유지
  * 트리 정점들 : MST 만들기 위해 선택된 정점들
  * 비트리 정점들 : 선택되지 않은 정점들

```python
import heapq

n, e = map(int, input().split())
G = [[] for _ in range(n)]
for _ in range(e):
  u, v, w = map(int, input().split())
  G[u].append((w, v))
  G[v].append((w, u))

visited = [0]*n
u = 0
visited[u] = 1

heap = []
# u와 연결된 간선 추가
for i in G[u]:
  heappush(heap, i)

total = 0
cnt = 0
while cnt < n-1:
  w, v = heappop(heap)
  if visited[v]:
    continue
  visited[v] = 1
  cnt += 1
  total += w
  for i in G[v]:
    if not visited[i[1]]:
      heappush(heap, i)

print(total)
```


# KRUSKAL 알고리즘
* 간선을 하나씩 선택해서 MST를 찾는 알고리즘
* 사이클을 만들지 않으면서, 비용이 작은 간선부터 차례대로 최소 신장 트리에 추가하는 그리디 알고리즘
* union find 알고리즘으로 구현
* `구현`
  * 간선 비용을 오름차순으로 정렬 후, 가장 낮은 비용부터 탐색
  * 간선으로 연결하는 정점 두개가 같은 그룹이라면, continue
  * 다른 그룹이라면, 같은 그룹으로 만들고 해당 간선을 최소 신장 트리에 추가
  * 최소 신장 트리에 v-1 개의 간선을 추가할 때 까지 반복
```python
def find_set(x):
  while x != p[x]:
    x = p[x]
  return x

def union(x, y):
  p[find_set(y)] = find_set(x)

def kruskal():
  n = v+1
  cnt, total = 0, 0
  for u, v, w in arr:
    if find_set(u) != find_set(v):
      cnt += 1
      union(u, v)
      total += w
      if cnt == n-1:
        return total

v, e = map(int, input().split())
arr = []
for _ in range(e):
  u, v, w = map(int, input().split())
  arr.append([u, v, w])

arr.sort(key=lambda x:x[2])
p = [i for i in range(v+1)]

print(kruskal())
```


# 최단 경로
* 간선의 가중치가 있는 그래프에서 간선의 가중치의 합이 최소인 경로
* 시작 정점에서 끝 정점까지의 최단 경로
  * 다익스트라 알고리즘 : 음의 가중치 허용 x
  * 벨만-포드 알고리즘 : 음의 가중치 허용 o
* 모든 정점들에 대한 최단 경로
  * 플로이드-워샬 알고리즘
## Dijkstra 알고리즘
