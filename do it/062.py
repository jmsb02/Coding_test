from math import inf

import sys

input = sys.stdin.readline

N, M = map(int, input().split())

edges = [0 for _ in range(M + 1)]
# 엣지 리스트 (1차원 리스트 - 출발 노드, 도착 노드, 비용)
for i in range(1, M + 1):
    A, B, C = map(int, input().split())
    edges[i] = (A, B, C)

# 최단 거리 리스트 (노드마다 "1번에서 여기까지의 최단거리"를 저장하는 배열)
D = [inf] * (N + 1)
D[1] = 0

# 벨만포드 N-1만큼 update
for i in range(1, N):
    for j in range(1, M + 1):
        A, B, C = edges[j]
        if D[A] != inf and D[A] + C < D[B]:
            D[B] = D[A] + C

minus = False

# 음수 사이클 존재 여부 확인
for i in range(1, M + 1):
    A, B, C = edges[i]
    if D[A] != inf and D[A] + C < D[B]:
        minus = True

if minus:
    print(-1)
else:
    # 1번 도시에서 다른 도시까지 가는 최단시간 출력 -> 2부터
    for i in range(2, N + 1):
        if D[i] == inf:
            print(-1)
        else:
            print(D[i])
