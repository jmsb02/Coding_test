import sys
from collections import deque

input = sys.stdin.readline

N, M, V = map(int, input().split())
graph = [[] for _ in range(N + 1)]  # 각 노드 번호마다 연결 목록 하나씩 필요

# graph(인접리스트) 만들기
for _ in range(1, M + 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# graph 오름차순 정렬
for i in range(1, N + 1):
    graph[i].sort()

# 방문 리스트
visited = [False] * (N + 1)


def DFS(v: int):
    if visited[v] == False:
        visited[v] = True
        print(v, end=" ")
        for i in graph[v]:
            DFS(i)


DFS(V)


def BFS(v: int):
    queue = deque()
    queue.append(v)
    visited[v] = True
    while queue:
        current = queue.popleft()
        print(current, end=" ")

        for i in graph[current]:
            if visited[i] == False:
                visited[i] = True
                queue.append(i)


print()
visited = [False] * (N + 1)
BFS(V)
