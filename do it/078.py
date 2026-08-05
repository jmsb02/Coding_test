from collections import deque
import sys

input = sys.stdin.readline

N = int(input())

# 1. 인접리스트
graph = [[] for _ in range(N + 1)]

for i in range(1, N):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 깊이 리스트 (N,M이 커서 BFS로)
depth = [0] * (N + 1)
visited = [False] * (N + 1)

# 시작 노드 (루트 노드 1번이라고 함)
queue = deque([1])
visited[1] = True

# 부모 리스트 (2**k> N 때의 K의 최솟값 찾고, 2차원 리스트를 만든다. 2차원 리스트 P = [K][N+1] (+1은 idx 고려))
K = 0
while 2**K <= N:
    K += 1
parent = [[0] * (N + 1) for _ in range(K)]


def BFS(n: int):
    while queue:
        v = queue.popleft()
        for node in graph[v]:
            if not visited[node]:
                visited[node] = True
                depth[node] = depth[v] + 1  # 내려가야 함
                # node 바로 위 부모가 누구인지 저장, node의 2^0 = 1칸 위 부모
                parent[0][node] = v
                queue.append(node)


# 탐색 노드 호출해서 값 채워 넣음
BFS(1)

# parent[0] 채웠으니 나머지도 다 채워줘야 함
# parent[K][N+1] (K = 행, N+1 = 열)
for i in range(1, K):
    for node in range(1, N + 1):
        parent[i][node] = parent[i - 1][parent[i - 1][node]]


#
def LCA(a: int, b: int):
    # 항상 a가 더 깊거나 같도록 맞춤 (코드를 한 방향으로 단순하게 만들기 위함)
    if depth[a] < depth[b]:
        a, b = b, a

    # depth_diff 구하고 실제 depth를 맞춰주는 과정
    depth_diff = depth[a] - depth[b]

    for k in range(K - 1, -1, -1):  # K를 큰 값부터 0까지 내려가며 확인
        if depth_diff >= 2**k:  # 2^k 만큼 점프할 수 있으면
            a = parent[k][a]  # 실제로 a를 위로 이동
            depth_diff -= 2**k  # 이동한 만큼 남은 차이 감소

    # depth를 맞췄을 때 같은 노드라면 그 노드가 LCA
    if a == b:
        return a

    for k in range(K - 1, -1, -1):  # 큰 점프부터 확인하면서
        if parent[k][a] != parent[k][b]:  # 조상이 다를 때만,
            a = parent[k][a]  # 위로 이동
            b = parent[k][b]
    # 마지막 반복문이 끝나면 a,b는 LCA가 아니라 LCA 바로 아래 서로 다른 노드에 존재
    return parent[0][a]


# 질의 처리
M = int(input())
for i in range(M):
    a, b = map(int, input().split())
    print(LCA(a, b))
