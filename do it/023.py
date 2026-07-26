n, m = map(int, input().split())
A = [[] for _ in range(n + 1)]
for i in range(1, m + 1):
    a, b = map(int, input().split())
    A[a].append(b)
    A[b].append(a)
visited = [False] * (n + 1)


def DFS(idx: int):  # DFS(1)
    visited[idx] = True  # visited[1] = True
    for i in A[idx]:  # 2,5
        if visited[i] == False:  # 2
            DFS(i)


cnt: int = 0
for i in range(1, n + 1):
    if visited[i] == False:
        DFS(i)
        cnt += 1
print(cnt)
