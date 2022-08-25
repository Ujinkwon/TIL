## B-0
def bfs(v, n):    # v 시작정점, n 마지막 정점 번호
    visited = [0] * (n+1)
    q = []
    q.append(v)
    visited[v] = 1
    while q:
        v = q.pop(0)
        print(v+1, end=' ')
        for w in l[v]:
            if not visited[w]:
                q.append(w)
                visited[w] = visited[w] + 1
n, m = map(int, input().split())
l = [[] for _ in range(n)]
ll = list(map(int, input().split()))
for i in range(0, m * 2, 2):
    l[ll[i] - 1].append(ll[i + 1]-1)
    l[ll[i+1]-1].append(ll[i]-1)
bfs(0, n)


## B-1
def bfs(s, g, v):    # v 정점개수
    visited = [0 for _ in range(v+1)]
    visited[s] = 1
    q = [s]
    while q:
        v = q.pop(0)
        if v == g:
            return visited[v] - 1
        for i in arr[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = visited[v] + 1
    return 0
t = int(input())
for tc in range(1, t+1):
    v, e = map(int, input().split())
    arr = [[] for _ in range(v+1)]
    for i in range(e):
        p, c = map(int, input().split())
        arr[p].append(c)
        arr[c].append(p)
    s, g = map(int, input().split())
    print(f'#{tc} {bfs(s, g, v)}')


## B-2
def bfs(i, j, n):
    visited = [[0]*n for _ in range(n+1)]
    q = [(i, j)]
    visited[i][j] = 1
    while q:
        i, j = q.pop(0)
        if maze[i][j] == 3:
            return visited[i][j] -2
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = i+di, j+dj
            if 0 <= ni < n and 0 <= nj < n and maze[ni][nj] != 1 and visited[ni][nj] == 0:
                q.append((ni, nj))
                visited[ni][nj] = visited[i][j] + 1
    return 0
t = int(input())
for tc in range(1, t+1):
    n = int(input())
    maze = [list(map(int, input())) for _ in range(n)]
    si = sj = -1
    for i in range(n):
        for j in range(n):
            if maze[i][j] == 2:
                si, sj = i, j
                break
        if si != -1:
            break
    print(f'#{tc} {bfs(si, sj, n)}')