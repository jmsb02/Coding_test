import sys

input = sys.stdin.readline

from math import inf

n = int(input())
m = int(input())

# 최단 거리 리스트 초기화
D = [[inf] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, n + 1):
        # 내 자신한테 가는 시간은 무조건 0 (나머지는 inf)
        if i == j:
            D[i][j] = 0

# 최단 거리 리스트 업데이트
for i in range(m):
    a, b, c = map(int, input().split())  # 3 4 2
    if c < D[a][b]:  # D[a][b] = 3 (기존에 있는 값이 새로 들어온 경로보다 크면)
        D[a][b] = c  # 최솟값 업데이트

# 플로이드-워셜
# 새로운 경로가 기존 경로보다 짧으면 기존 경로를 업데이트 해준다.
for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if D[i][k] + D[k][j] < D[i][j]:
                D[i][j] = D[i][k] + D[k][j]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if D[i][j] == inf:
            print(0, end=" ")
        else:
            print(D[i][j], end=" ")
    print()
