from math import inf
from queue import PriorityQueue

import sys

input = sys.stdin.readline

V, E = map(int, input().split())
K = int(input())

graph = [[] for _ in range(V + 1)]
# 인접리스트
D = [inf] * (V + 1)
D[K] = 0  # 시작 노드까지의 최단거리를 0으로 설정

# 인접 리스트 초기화
for i in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

# 다익스트라 -> 우선순위 큐 사용
queue = PriorityQueue()
queue.put((0, K))  # tuple 형식! (시작 거리, 시작 노드)

while not queue.empty():
    node_distance, node = queue.get()  # 0, 1
    # ex) 이미 (5,2)로 최단 경로 구했는데 뒤에 (10,2) 나오는 경우
    if D[node] < node_distance:
        continue

    # 인접한 노드들 돌면서
    for next_node, next_distance in graph[node]:  # [[2,2], [3,3]]
        # 최솟값으로 update 해줘야 하니까 지금 값이 더 커야지
        if D[node] + next_distance < D[next_node]:
            D[next_node] = min(D[next_node], D[node] + next_distance)
            # 다익스트라가 구하고자 하는 것 : 시작점에서 각 노드까지 가는 전체 비용이기 때문에 누적 거리를 넣어줘야 함
            queue.put((node_distance + next_distance, next_node))
for i in range(1, V + 1):
    print(D[i])
