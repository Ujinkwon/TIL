adjlist = [
    [1, 2], 
    [0, 3, 4], 
    [0, 4], 
    [1, 5], 
    [1, 2, 5], 
    [3, 4, 6], 
    [5]
]


def bfs(v, n):    # v 시작정점, n 마지막 정점 번호
    visited = [0] * (n+1)
    q = []
    q.append(v)
    visited[v] = 1
    while q:
        v = q.pop(0)
        print(v)
        for w in adjlist[v]:
            if not visited[w]:
                q.append(w)
                visited[w] = visited[w] + 1


def bfs(v, n, t):    # v 시작정점, n 마지막 정점 번호, t 찾는 정점
    visited = [0] * (n+1)
    q = []
    q.append(v)
    visited[v] = 1
    while q:
        v = q.pop(0)
        if v == t:
            return visited[99]
        for w in adjlist[v]:
            if not visited[w]:
                q.append(w)
                visited[w] = visited[v] + 1
    return 0





# 미로
def bfs(i, j, n):    # v 시작정점, n 마지막 정점 번호, t 찾는 정점
    visited = [[0]*n for _ in range(n)]
    q = []
    q.append((i, j))
    visited[i][j] = 1
    while q:
        i, j = q.pop(0)
        if maze[i][j] == 3:
            return 1
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = i+di, j+dj
            if 0 <= ni < n and 0 <= nj < n and maze[ni][nj] != 1 and visited[ni][nj] == 0:
                q.append((ni, nj))
                visited[ni][nj] = visited[i][j] + 1                
    return 0

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    maze = [list(map(int, input().split())) for _ in range(n)]
    sti = -1
    stj = -1
    for i in range(n):
        for j in range(n):
            if maze[i][j] == 2:
                sti, stj = i, j
                break
        if sti != -1:
            break
    bfs(sti, stj, n)



def dfs(i, j, n):
    if maze[i][j] == 3:
        return 1
    else:
        visited[i][j] = 1
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = i+di, j+dj
            if maze[ni][nj] != 1 and visited[ni][nj] == 0:
                dfs(ni, nj, n)
        visited[i][j] = 0
        return 0

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    maze = [list(map(int, input().split())) for _ in range(n)]
    sti = -1
    stj = -1
    for i in range(n):
        for j in range(n):
            if maze[i][j] == 2:
                sti, stj = i, j
                break
        if sti != -1:
            break
    visited = [[0]*n for _ in range(n)]
    dfs(sti, stj, n)